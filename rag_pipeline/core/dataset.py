import pandas as pd
import logging
import os
import json
import ast
from typing import List, Optional, Dict

from .models import RAGTestCase, RAGDocument

logger = logging.getLogger(__name__)

class RAGDataset:
    """Handles loading and managing RAG evaluation datasets"""
    
    def __init__(self, dataset_path: Optional[str] = None):
        self.dataset_path = dataset_path
        self.test_cases: List[RAGTestCase] = []
        self.documents: List[RAGDocument] = []
    
    def load_test_cases(self, queries_file: Optional[str] = None) -> List[RAGTestCase]:
        """Load test cases from CSV file"""
        
        # Determine queries file path
        if queries_file:
            queries_path = queries_file
        elif self.dataset_path:
            queries_path = self.dataset_path
        else:
            # Use default queries file
            queries_path = os.path.join(
                "rag_pipeline",
                "default_datasets",
                "retrieval_withgen.csv"
            )
        
        try:
            logger.info(f"Loading test cases from: {queries_path}")
            
            # Read CSV file
            df = pd.read_csv(
                queries_path,
                quotechar='"',
                escapechar=None,
                skipinitialspace=True,
                na_filter=False,
                keep_default_na=False
            )
            
            test_cases = []
            for idx, row in df.iterrows():
                try:
                    # Parse additional_args to get relevant document IDs
                    additional_args = row.get("additional_args", "{}")
                    if isinstance(additional_args, str):
                        try:
                            additional_args = json.loads(additional_args)
                        except (json.JSONDecodeError, ValueError):
                            try:
                                additional_args = ast.literal_eval(additional_args)
                            except (ValueError, SyntaxError):
                                additional_args = {}
                    
                    relevant_doc_ids = additional_args.get("true_qrel_list", [])
                    if isinstance(relevant_doc_ids, str):
                        relevant_doc_ids = [relevant_doc_ids]
                    
                    test_case = RAGTestCase(
                        id=str(row.get("id", idx)),
                        query=row.get("user_prompt", ""),
                        ground_truth_answer=row.get("ground_truth", ""),
                        relevant_doc_ids=relevant_doc_ids,
                        metadata={
                            "task": row.get("task", "retrieval"),
                            "original_index": idx
                        }
                    )
                    test_cases.append(test_case)
                    
                except Exception as e:
                    logger.warning(f"Failed to parse test case at row {idx}: {e}")
                    continue
            
            logger.info(f"Loaded {len(test_cases)} test cases")
            self.test_cases = test_cases
            return test_cases
            
        except Exception as e:
            logger.error(f"Failed to load test cases from {queries_path}: {e}")
            return []
    
    def load_documents(self, docs_file: Optional[str] = None) -> List[RAGDocument]:
        """Load knowledge base documents from CSV file"""
        
        # Determine documents file path
        if docs_file:
            docs_path = docs_file
        else:
            # Use default docs file
            docs_path = os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                "default_datasets",
                "retrieval_docs.csv"
            )
        
        try:
            logger.info(f"Loading documents from: {docs_path}")
            
            # Read CSV file
            df = pd.read_csv(
                docs_path,
                quotechar='"',
                escapechar=None,
                skipinitialspace=True,
                na_filter=False,
                keep_default_na=False
            )
            
            documents = []
            for idx, row in df.iterrows():
                try:
                    # Parse metadata
                    metadata = row.get("metadata", "{}")
                    if isinstance(metadata, str):
                        try:
                            metadata = json.loads(metadata)
                        except (json.JSONDecodeError, ValueError):
                            try:
                                metadata = ast.literal_eval(metadata)
                            except (ValueError, SyntaxError):
                                metadata = {}
                    
                    # Get doc_id from metadata or use index
                    doc_id = metadata.get('doc_id', str(idx))
                    
                    document = RAGDocument(
                        doc_id=str(doc_id),
                        content=row.get("text", ""),
                        metadata=metadata
                    )
                    documents.append(document)
                    
                except Exception as e:
                    logger.warning(f"Failed to parse document at row {idx}: {e}")
                    continue
            
            logger.info(f"Loaded {len(documents)} documents")
            self.documents = documents
            return documents
            
        except Exception as e:
            logger.error(f"Failed to load documents from {docs_path}: {e}")
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