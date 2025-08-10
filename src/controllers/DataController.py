from .BaseController import BaseController
from models import ResponseSignal
from fastapi import UploadFile

class DataController(BaseController):
    
    def __init__(self):
        super().__init__()
        self.size_scale = 1024*1024 #from mega to bytes
    def validate_file(self , file : UploadFile):
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False , ResponseSignal.FILE_NOT_SUPPORT.value
        if file.size > self.app_settings.FILE_MAX_SIZE* self.size_scale:
            return False , ResponseSignal.FILE_SIZE_EXCEED.value
        
        return True , ResponseSignal.FILE_VALID_SUCCESS.value