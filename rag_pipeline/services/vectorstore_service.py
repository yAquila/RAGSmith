"""Vectorstore Management Service"""

import os
import logging
from typing import Dict, Any, Optional

logger = logging.getLogger(__name__)


class VectorstoreService:
    """Service for managing vectorstore operations"""
    
    def __init__(self, dataset_service=None):
        self.logger = logging.getLogger(__name__)
        self.dataset_service = dataset_service
        self._current_docs_path = None
        self._current_dataset_hash = None

    def get_or_create_vectorstore(self, embedding_model: str, force_rebuild: bool = False):
        """Get or create vectorstore for retrieval tasks"""
        try:
            # Import vectorstore utilities
            from util.vectorstore import QdrantVectorStore
            from util.vectorstore.dataset_utils import load_retrieval_docs, generate_dataset_hash_from_file

            # Determine which documents file to use
            docs_path = None
            
            # # Check if dataset service has an uploaded documents file
            # if self.dataset_service:
            #     uploaded_docs_path = self.dataset_service.get_retrieval_docs_file_path()
            #     if uploaded_docs_path and os.path.exists(uploaded_docs_path):
            #         docs_path = uploaded_docs_path
            #         self.logger.info(f"Using uploaded documents file: {docs_path}")
            
            # # Check if we have an uploaded documents file from retrieval dataset loading (fallback)
            # if not docs_path and hasattr(self, '_retrieval_docs_file_path') and self._retrieval_docs_file_path:
            #     docs_path = self._retrieval_docs_file_path
            #     self.logger.info(f"Using uploaded documents file: {docs_path}")
            
            # Use default documents file if no uploaded file found
            if not docs_path:
                docs_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "default_datasets", "retrieval_docs.csv")
                self.logger.info(f"Using default documents file: {docs_path}")
            
            # Generate dataset hash from the documents file
            dataset_hash = generate_dataset_hash_from_file(docs_path)
            
            # Create vectorstore instance with dataset hash
            vectorstore = QdrantVectorStore(embedding_model, dataset_hash)
            
            retrieval_docs = load_retrieval_docs(docs_path)
            # Index documents with enhanced resumption capabilities
            self.logger.info(f"Starting indexing process for {embedding_model} with dataset {dataset_hash[:8]}")
            success = vectorstore.index_documents(retrieval_docs, force_reindex=force_rebuild)
            
            if success:
                return vectorstore
            else:
                self.logger.error(f"Failed to index documents for {embedding_model}")
                return None
                
        except Exception as e:
            self.logger.error(f"Error creating vectorstore for {embedding_model}: {e}")
            import traceback
            self.logger.error(f"Traceback: {traceback.format_exc()}")
            return None
    
    def get_vectorstore_info(self, embedding_model: str, dataset_hash: str = None) -> Dict[str, Any]:
        """Get information about a vectorstore"""
        try:
            from util.vectorstore import QdrantVectorStore
            from util.vectorstore.dataset_utils import generate_dataset_hash_from_file
            
            docs_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "default_datasets", "retrieval_docs.csv")
            if not dataset_hash:
                dataset_hash = generate_dataset_hash_from_file(docs_path)
            
            vectorstore = QdrantVectorStore(embedding_model, dataset_hash)
            return vectorstore.get_collection_info()
            
        except Exception as e:
            self.logger.error(f"Error getting vectorstore info: {e}")
            return {"error": str(e)}
    
    def rebuild_vectorstore(self, embedding_model: str) -> bool:
        """Rebuild vectorstore for a specific embedding model"""
        try:
            self.logger.info(f"Rebuilding vectorstore for {embedding_model}")
            vectorstore = self.get_or_create_vectorstore(embedding_model, force_rebuild=True)
            return vectorstore is not None
        except Exception as e:
            self.logger.error(f"Error rebuilding vectorstore: {e}")
            return False
    
    def clear_vectorstore(self, embedding_model: str, dataset_hash: str = None, completely_delete: bool = False) -> bool:
        """Clear a specific vectorstore"""
        try:
            from util.vectorstore import QdrantVectorStore
            from util.vectorstore.dataset_utils import generate_dataset_hash_from_file
            
            if dataset_hash:
                # Clear specific dataset+model combination
                vectorstore = QdrantVectorStore(embedding_model, dataset_hash)
                
                if completely_delete:
                    vectorstore.delete_collection_completely()
                    action = "completely deleted"
                else:
                    vectorstore.clear_collection()
                    action = "cleared"
                
                self.logger.info(f"{action.capitalize()} vectorstore for {embedding_model} with dataset {dataset_hash[:8]}")
                return True
            else:
                # Clear all vectorstores for this embedding model
                success_count = 0
                
                action = "completely deleted" if completely_delete else "cleared"
                self.logger.info(f"{action.capitalize()} {success_count} vectorstore(s) for {embedding_model}")
                return success_count > 0
                
        except Exception as e:
            self.logger.error(f"Error clearing vectorstore for {embedding_model}: {e}")
            return False
    
    def clear_all_vectorstores(self) -> bool:
        """COMPLETELY delete all vectorstore collections (factory reset)"""
        try:
            # Also check for any collections in Qdrant that match our pattern
            from util.vectorstore import QdrantVectorStore
            
            # Create a temporary vectorstore to access Qdrant client
            try:
                temp_vectorstore = QdrantVectorStore("temp_model", "temp_hash", "temp")
                collections = temp_vectorstore.client.get_collections().collections
            except Exception as e:
                self.logger.error(f"Error accessing Qdrant client: {e}")
                return False
            
            collections_to_delete = []
            for collection in collections:
                if collection.name.startswith("retrieval_benchmark_"):
                    try:
                        # Parse new format: retrieval_benchmark_{dataset_hash}_{embedding_model}
                        parts = collection.name.replace("retrieval_benchmark_", "").split("_")
                        if len(parts) >= 2:
                            dataset_hash = parts[0]
                            model_parts = parts[1:]
                            model_name = "-".join(model_parts)
                            collections_to_delete.append((model_name, dataset_hash, collection.name))
                    except Exception as e:
                        self.logger.warning(f"Could not parse collection name {collection.name}: {e}")
                        # Still try to delete it if it matches the pattern
                        collections_to_delete.append(("unknown", "unknown", collection.name))
            
            # COMPLETELY DELETE all vectorstore collections (factory reset)
            success_count = 0
            total_count = len(collections_to_delete)
            
            for model_name, dataset_hash, collection_name in collections_to_delete:
                try:
                    # Create vectorstore instance and completely delete collection
                    vectorstore = QdrantVectorStore(model_name, dataset_hash)
                    vectorstore.delete_collection_completely()  # Use the new complete deletion method
                    success_count += 1
                    self.logger.info(f"Completely deleted collection: {collection_name}")
                except Exception as e:
                    self.logger.error(f"Error completely deleting collection {collection_name}: {e}")
            
            
            self.logger.info(f"Factory reset complete: Completely deleted {success_count}/{total_count} collections")
            return success_count == total_count
        except Exception as e:
            self.logger.error(f"Error during factory reset: {e}")
            return False
    
    def get_all_vectorstore_info(self) -> Dict[str, Any]:
        """Get information about all vectorstores"""
        try:
            from util.vectorstore import QdrantVectorStore
            
            # Create a temporary vectorstore to access Qdrant client - need proper args now
            try:
                temp_vectorstore = QdrantVectorStore("temp_model", "temp_hash", "temp")
                collections = temp_vectorstore.client.get_collections().collections
            except Exception as e:
                self.logger.error(f"Error accessing Qdrant client: {e}")
                return {"error": f"Cannot access Qdrant: {str(e)}"}
            
            vectorstore_info = {}
            for collection in collections:
                if collection.name.startswith("retrieval_benchmark_"):
                    try:
                        # New format: retrieval_benchmark_{dataset_hash}_{embedding_model}
                        parts = collection.name.replace("retrieval_benchmark_", "").split("_")
                        if len(parts) >= 2:
                            # Extract dataset hash (first part) and reconstruct model name (remaining parts)
                            dataset_hash = parts[0]
                            model_parts = parts[1:]
                            model_name = "-".join(model_parts)
                            
                            # Create key with both dataset and model info
                            key = f"{model_name}-{dataset_hash}"
                            
                            try:
                                vectorstore = QdrantVectorStore(model_name, dataset_hash)
                                info = vectorstore.get_collection_info()
                                info["model_name"] = model_name
                                info["dataset_hash"] = dataset_hash
                                vectorstore_info[key] = info
                            except Exception as e:
                                vectorstore_info[key] = {
                                    "error": str(e),
                                    "model_name": model_name,
                                    "dataset_hash": dataset_hash
                                }
                    except Exception as e:
                        # Fallback for collections that don't match expected format
                        vectorstore_info[collection.name] = {"error": f"Invalid collection format: {str(e)}"}
            
            return vectorstore_info
        except Exception as e:
            self.logger.error(f"Error getting all vectorstore info: {e}")
            return {"error": str(e)}
    
    def set_retrieval_docs_file_path(self, file_path: str):
        """Set the retrieval documents file path"""
        self._retrieval_docs_file_path = file_path 