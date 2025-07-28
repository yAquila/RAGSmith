import pandas as pd
import logging
import os
import json
import ast
from typing import List, Optional, Dict
from pathlib import Path

from .models import RAGTestCase, RAGDocument

logger = logging.getLogger(__name__)

class RAGDataset:
    """Handles loading and managing RAG evaluation datasets"""
    
    def __init__(self, dataset_path: Optional[str] = None):
        self.dataset_path = dataset_path
        self.test_cases: List[RAGTestCase] = []
        self.documents: List[RAGDocument] = []
    
    def load_test_cases(self, dataset_folder: Optional[str] = None) -> List[RAGTestCase]:
        """Load test cases from JSON files in the specified folder"""
        
        # Determine dataset folder path
        if dataset_folder:
            folder_path = dataset_folder
        elif self.dataset_path:
            folder_path = self.dataset_path
        else:
            # Use default dataset folder
            folder_path = os.path.join(
                "rag_pipeline",
                "default_datasets",
                "gen_programming_10"
            )
        
        try:
            logger.info(f"Loading test cases from folder: {folder_path}")
            
            test_cases = []
            json_files = list(Path(folder_path).glob("*.json"))
            
            if not json_files:
                logger.warning(f"No JSON files found in {folder_path}")
                return []
            
            for json_file in json_files:
                try:
                    with open(json_file, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    
                    # Extract questions from the JSON file
                    questions_data = data.get("questions", {})
                    questions = questions_data.get("items", [])
                    
                    for idx, question_data in enumerate(questions):
                        try:
                            # Extract relevant chunk IDs (previously true_qrel_list)
                            related_chunk_ids = question_data.get("related_chunk_ids", [])
                            if isinstance(related_chunk_ids, str):
                                related_chunk_ids = [related_chunk_ids]
                            
                            # Create test case
                            test_case = RAGTestCase(
                                id=f"{json_file.stem}_q{idx}",
                                query=question_data.get("question", ""),
                                ground_truth_answer=question_data.get("answer", ""),
                                relevant_doc_ids=related_chunk_ids,
                                metadata={
                                    "task": "retrieval",
                                    "source_file": json_file.name,
                                    "category": question_data.get("category", "FACTUAL"),
                                    "original_index": idx
                                }
                            )
                            test_cases.append(test_case)
                            
                        except Exception as e:
                            logger.warning(f"Failed to parse question {idx} in {json_file.name}: {e}")
                            continue
                    
                except Exception as e:
                    logger.warning(f"Failed to load JSON file {json_file}: {e}")
                    continue
            
            logger.info(f"Loaded {len(test_cases)} test cases from {len(json_files)} files")
            self.test_cases = test_cases
            return test_cases
            
        except Exception as e:
            logger.error(f"Failed to load test cases from {folder_path}: {e}")
            return []
    
    def load_documents(self, dataset_folder: Optional[str] = None) -> List[RAGDocument]:
        """Load knowledge base documents from JSON files in the specified folder"""
        
        # Determine dataset folder path
        if dataset_folder:
            folder_path = dataset_folder
        elif self.dataset_path:
            folder_path = self.dataset_path
        else:
            # Use default dataset folder
            folder_path = os.path.join(
                "rag_pipeline",
                "default_datasets",
                "gen_programming_10"
            )
        
        try:
            logger.info(f"Loading documents from folder: {folder_path}")
            
            documents = []
            json_files = list(Path(folder_path).glob("*.json"))
            
            if not json_files:
                logger.warning(f"No JSON files found in {folder_path}")
                return []
            
            for json_file in json_files:
                try:
                    with open(json_file, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    
                    # Extract article and chunks from the JSON file
                    article_data = data.get("article", {})
                    chunks_data = data.get("chunks", [])
                    
                    # Create document for each chunk
                    for chunk in chunks_data:
                        try:
                            # Create metadata for the chunk
                            metadata = {
                                "article_id": article_data.get("id", ""),
                                "article_title": article_data.get("title", ""),
                                "article_url": article_data.get("url", ""),
                                "chunk_id": chunk.get("id", ""),
                                "section": chunk.get("section", ""),
                                "heading_path": chunk.get("heading_path", ""),
                                "start_char": chunk.get("start_char", 0),
                                "end_char": chunk.get("end_char", 0),
                                "char_count": chunk.get("char_count", 0),
                                "token_estimate": chunk.get("token_estimate", 0),
                                "source_file": json_file.name
                            }
                            
                            document = RAGDocument(
                                doc_id=chunk.get("id", ""),
                                content=chunk.get("content", ""),
                                metadata=metadata
                            )
                            documents.append(document)
                            
                        except Exception as e:
                            logger.warning(f"Failed to parse chunk in {json_file.name}: {e}")
                            continue
                    
                except Exception as e:
                    logger.warning(f"Failed to load JSON file {json_file}: {e}")
                    continue
            
            logger.info(f"Loaded {len(documents)} documents from {len(json_files)} files")
            self.documents = documents
            return documents
            
        except Exception as e:
            logger.error(f"Failed to load documents from {folder_path}: {e}")
            return []
    
    def get_test_cases(self, max_cases: Optional[int] = None) -> List[RAGTestCase]:
        """Get test cases, optionally limited by max_cases"""
        if not self.test_cases:
            self.load_test_cases()
        
        if max_cases and max_cases > 0:
            return self.test_cases[:max_cases]
        return self.test_cases
    
    def get_documents(self) -> List[RAGDocument]:
        """Get all documents"""
        if not self.documents:
            self.load_documents()
        return self.documents
    
    def validate_dataset(self) -> Dict[str, any]:
        """Validate the loaded dataset"""
        test_cases = self.get_test_cases()
        documents = self.get_documents()
        
        validation_result = {
            "valid": True,
            "test_cases_count": len(test_cases),
            "documents_count": len(documents),
            "issues": []
        }
        
        # Check if we have test cases
        if not test_cases:
            validation_result["valid"] = False
            validation_result["issues"].append("No test cases loaded")
        
        # Check if we have documents
        if not documents:
            validation_result["valid"] = False
            validation_result["issues"].append("No documents loaded")
        
        # Check for test cases with missing ground truth
        missing_ground_truth = sum(1 for tc in test_cases if not tc.ground_truth_answer.strip())
        if missing_ground_truth > 0:
            validation_result["issues"].append(f"{missing_ground_truth} test cases missing ground truth")
        
        # Check for test cases with no relevant documents
        no_relevant_docs = sum(1 for tc in test_cases if not tc.relevant_doc_ids)
        if no_relevant_docs > 0:
            validation_result["issues"].append(f"{no_relevant_docs} test cases have no relevant documents")
        
        # Get document IDs for validation
        document_ids = set(doc.doc_id for doc in documents)
        
        # Check for missing referenced documents
        missing_docs = set()
        for test_case in test_cases:
            for doc_id in test_case.relevant_doc_ids:
                if str(doc_id) not in document_ids:
                    missing_docs.add(str(doc_id))
        
        if missing_docs:
            validation_result["issues"].append(f"Missing documents referenced in test cases: {list(missing_docs)[:10]}")
        
        logger.info(f"Dataset validation: {validation_result}")
        return validation_result 