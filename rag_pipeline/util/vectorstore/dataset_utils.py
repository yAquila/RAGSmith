"""
Dataset utilities for vector store operations.

Provides utilities for:
- Dataset hashing
- CSV loading with proper formatting
- Metadata parsing and validation
"""

import logging
import pandas as pd
import ast
import json
import hashlib
import os

logger = logging.getLogger(__name__)


def generate_dataset_hash_from_file(file_path: str) -> str:
    """
    Generate a hash for dataset file to create unique collection names
    
    Args:
        file_path: Path to the dataset CSV file
        
    Returns:
        MD5 hash string of the dataset content
    """
    try:
        # Load the dataset
        df = pd.read_csv(
            file_path,
            quotechar='"',
            escapechar=None,
            skipinitialspace=True,
            na_filter=False,
            keep_default_na=False
        )
        
        # Generate hash based on content
        content_hashes = []
        for idx, row in df.iterrows():
            text = row['text'] if 'text' in row else str(row.get('user_prompt', ''))
            metadata_str = row.get('metadata', str(idx))
            try:
                metadata = ast.literal_eval(metadata_str) if isinstance(metadata_str, str) else metadata_str
            except:
                try:
                    metadata = json.loads(metadata_str) if isinstance(metadata_str, str) else metadata_str
                except:
                    metadata = {"doc_id": str(idx)}
            
            doc_id = metadata.get('doc_id', str(idx))
            content = f"{doc_id}:{text}"
            content_hashes.append(hashlib.md5(content.encode()).hexdigest())
        
        # Sort and combine all hashes to create dataset hash
        content_hashes.sort()
        combined_content = "".join(content_hashes)
        return hashlib.md5(combined_content.encode()).hexdigest()
        
    except Exception as e:
        logger.error(f"Error generating dataset hash from {file_path}: {e}")
        # Fallback: use file name and size
        if os.path.exists(file_path):
            file_stat = os.stat(file_path)
            fallback_content = f"{os.path.basename(file_path)}_{file_stat.st_size}_{file_stat.st_mtime}"
            return hashlib.md5(fallback_content.encode()).hexdigest()
        else:
            return hashlib.md5(file_path.encode()).hexdigest()


def generate_dataset_hash_from_dataframe(df: pd.DataFrame) -> str:
    """
    Generate a hash for dataset dataframe to create unique collection names
    
    Args:
        df: Pandas DataFrame containing the dataset
        
    Returns:
        MD5 hash string of the dataset content
    """
    try:
        # Generate hash based on content
        content_hashes = []
        for idx, row in df.iterrows():
            text = row['text'] if 'text' in row else str(row.get('user_prompt', ''))
            metadata_str = row.get('metadata', str(idx))
            try:
                metadata = ast.literal_eval(metadata_str) if isinstance(metadata_str, str) else metadata_str
            except:
                try:
                    metadata = json.loads(metadata_str) if isinstance(metadata_str, str) else metadata_str
                except:
                    metadata = {"doc_id": str(idx)}
            
            doc_id = metadata.get('doc_id', str(idx))
            content = f"{doc_id}:{text}"
            content_hashes.append(hashlib.md5(content.encode()).hexdigest())
        
        # Sort and combine all hashes to create dataset hash
        content_hashes.sort()
        combined_content = "".join(content_hashes)
        return hashlib.md5(combined_content.encode()).hexdigest()
        
    except Exception as e:
        logger.error(f"Error generating dataset hash from dataframe: {e}")
        # Fallback: use DataFrame info
        fallback_content = f"df_{len(df)}_{df.shape[1]}"
        return hashlib.md5(fallback_content.encode()).hexdigest()


def load_retrieval_docs(file_path: str) -> pd.DataFrame:
    """
    Load retrieval documents from CSV file
    
    Args:
        file_path: Path to the retrieval documents CSV file
        
    Returns:
        DataFrame containing the documents with 'text' and 'metadata' columns
    """
    try:
        df = pd.read_csv(
            file_path,
            quotechar='"',
            escapechar=None,
            skipinitialspace=True,
            na_filter=False,
            keep_default_na=False,
            encoding='utf-8'
        )
        logger.info(f"Loaded {len(df)} documents from {file_path}")
        return df
    except Exception as e:
        logger.error(f"Error loading retrieval docs: {e}")
        raise


def load_retrieval_queries(file_path: str) -> pd.DataFrame:
    """
    Load retrieval queries from CSV file
    
    Args:
        file_path: Path to the retrieval queries CSV file
        
    Returns:
        DataFrame containing the queries with parsed 'qrel' column
    """
    try:
        df = pd.read_csv(
            file_path,
            quotechar='"',
            escapechar=None,
            skipinitialspace=True,
            na_filter=False,
            keep_default_na=False,
            encoding='utf-8'
        )
        
        # Parse qrel column (it's stored as string representation of list)
        def parse_qrel(qrel_str):
            try:
                return ast.literal_eval(qrel_str)
            except:
                try:
                    return json.loads(qrel_str)
                except:
                    logger.warning(f"Failed to parse qrel: {qrel_str}")
                    return []
        
        df['qrel'] = df['qrel'].apply(parse_qrel)
        
        logger.info(f"Loaded {len(df)} queries from {file_path}")
        return df
    except Exception as e:
        logger.error(f"Error loading retrieval queries: {e}")
        raise 