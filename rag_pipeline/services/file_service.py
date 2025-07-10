"""File Management Service"""

import os
import uuid
import asyncio
import logging
import aiofiles
from typing import Dict, Any, List, Optional
from datetime import datetime, timedelta, timezone
from pathlib import Path
from fastapi import UploadFile, HTTPException

# Configure timezone
GMT_PLUS_3 = timezone(timedelta(hours=3))

logger = logging.getLogger(__name__)


class FileService:
    """Service for handling file upload, validation, and management operations"""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        
        # Constants for file storage
        self.temp_upload_dir = "/tmp/rag_pipeline_uploads"
        self.max_file_size = 50 * 1024 * 1024  # 50MB max file size
        self.allowed_extensions = {'.csv'}
        self.cleanup_hours = 24  # Clean up files older than 24 hours
        
        # Ensure upload directory exists
        os.makedirs(self.temp_upload_dir, exist_ok=True)
        
        # File storage dictionary (will be set from main.py)
        self._uploaded_files: Dict[str, Dict[str, Any]] = {}
    
    def set_uploaded_files_reference(self, uploaded_files_dict: Dict[str, Any]):
        """Set reference to uploaded files dictionary from main module"""
        self._uploaded_files = uploaded_files_dict
    
    def validate_file_upload(self, file: UploadFile) -> None:
        """Validate uploaded file basic properties"""
        if not file.filename:
            raise Exception("No file selected")
        
        # Check file extension
        file_extension = Path(file.filename).suffix.lower()
        if file_extension not in self.allowed_extensions:
            raise Exception(f"File type '{file_extension}' not allowed. Only CSV files are accepted.")
        
        # Note: file.size is not available in FastAPI UploadFile, so we'll check size during read
    
    async def save_uploaded_file(self, file: UploadFile) -> str:
        """Save uploaded file to temporary directory and return file ID"""
        # Create upload directory if it doesn't exist
        os.makedirs(self.temp_upload_dir, exist_ok=True)
        
        # Generate unique file ID
        file_id = str(uuid.uuid4())
        
        # Create safe filename with UUID prefix
        original_name = file.filename or "unknown.csv"
        safe_filename = f"{file_id}_{original_name}"
        file_path = os.path.join(self.temp_upload_dir, safe_filename)
        
        self.logger.info(f"Saving uploaded file: {original_name} -> {file_path}")
        
        try:
            # Save file to disk
            async with aiofiles.open(file_path, 'wb') as f:
                content = await file.read()
                await f.write(content)
            
            # Store file information
            file_info = {
                "file_id": file_id,
                "original_name": original_name,
                "file_path": file_path,
                "size": len(content),
                "upload_time": datetime.now(GMT_PLUS_3)
            }
            
            self._uploaded_files[file_id] = file_info
            self.logger.info(f"Saved uploaded file: {original_name} -> {file_path}")
            self.logger.info(f"File info stored with ID: {file_id}, size: {len(content)} bytes")
            
            return file_id
            
        except Exception as e:
            self.logger.error(f"Failed to save uploaded file {original_name}: {str(e)}")
            # Clean up on failure
            if os.path.exists(file_path):
                try:
                    os.unlink(file_path)
                    self.logger.info(f"Cleaned up failed upload file: {file_path}")
                except:
                    pass
            raise
    
    async def delete_uploaded_file(self, file_id: str) -> bool:
        """Delete an uploaded file"""
        try:
            if file_id not in self._uploaded_files:
                self.logger.warning(f"Attempted to delete non-existent file ID: {file_id}")
                return False
            
            file_info = self._uploaded_files[file_id]
            file_path = file_info["file_path"]
            
            self.logger.info(f"Deleting uploaded file: {file_id} -> {file_path}")
            
            # Remove file if it exists
            if os.path.exists(file_path):
                os.unlink(file_path)
                self.logger.info(f"File deleted from disk: {file_path}")
            
            # Remove from tracking
            del self._uploaded_files[file_id]
            self.logger.info(f"File info removed for ID: {file_id}")
            
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to delete uploaded file {file_id}: {str(e)}")
            return False
    
    def list_uploaded_files(self) -> List[Dict[str, Any]]:
        """List all uploaded dataset files"""
        files_list = []
        for file_id, file_info in self._uploaded_files.items():
            files_list.append({
                "file_id": file_id,
                "original_name": file_info["original_name"],
                "file_size": file_info["size"],
                "upload_time": file_info["upload_time"].isoformat()
            })
        return files_list
    
    def get_file_path(self, file_id: str) -> Optional[str]:
        """Get file path for a given file ID"""
        file_info = self._uploaded_files.get(file_id)
        if file_info and os.path.exists(file_info["file_path"]):
            return file_info["file_path"]
        return None
    
    def get_file_info(self, file_id: str) -> Optional[Dict[str, Any]]:
        """Get file information for a given file ID"""
        return self._uploaded_files.get(file_id)

    def add_file_metadata(self, file_id: str, metadata: Dict[str, Any]) -> None:
        """Add metadata to an uploaded file"""
        if file_id in self._uploaded_files:
            self._uploaded_files[file_id].update(metadata)
    
    async def cleanup_old_files(self) -> None:
        """Remove uploaded files older than 24 hours"""
        if not os.path.exists(self.temp_upload_dir):
            return
        
        self.logger.info("Starting cleanup of old uploaded files")
        cutoff_time = datetime.now(GMT_PLUS_3) - timedelta(hours=self.cleanup_hours)
        cleaned_count = 0
        error_count = 0
        
        # Create a copy of the keys to avoid modification during iteration
        file_ids_to_check = list(self._uploaded_files.keys())
        
        for file_id in file_ids_to_check:
            try:
                file_info = self._uploaded_files[file_id]
                if file_info["upload_time"] < cutoff_time:
                    file_path = file_info["file_path"]
                    
                    # Remove file if it exists
                    if os.path.exists(file_path):
                        os.unlink(file_path)
                        self.logger.info(f"Deleted old file: {file_path}")
                    
                    # Remove from tracking
                    del self._uploaded_files[file_id]
                    cleaned_count += 1
                    self.logger.info(f"Removed file info for expired file ID: {file_id}")
                    
            except Exception as e:
                self.logger.error(f"Error cleaning up file {file_id}: {str(e)}")
                error_count += 1
        
        self.logger.info(f"File cleanup completed: {cleaned_count} files cleaned up, {error_count} errors")
    
    async def start_periodic_cleanup(self) -> None:
        """Start periodic cleanup of old files"""
        while True:
            await self.cleanup_old_files()
            await asyncio.sleep(3600)  # Run every hour 