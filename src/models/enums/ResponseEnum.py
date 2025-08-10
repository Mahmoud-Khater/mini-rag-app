from enum import Enum

class ResponseSignal(Enum):
    FILE_VALID_SUCCESS = "file success"
    FILE_NOT_SUPPORT = "file not support"
    FILE_SIZE_EXCEED = "file size exceed"
    FILE_UPLOAD_SUCCESS = "file upload success"
    FILE_UPLOAD_FAILED = "file upload failed"