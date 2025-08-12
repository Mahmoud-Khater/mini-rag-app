from .BaseController import BaseController
from .ProjectController import ProjectController
from models import ResponseSignal
from fastapi import UploadFile
import re
import os

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
    def get_clean_file_name(self, file_name : str):

        #remove special chars except . and underscore
        clean_name = re.sub(r'[^\w.]','',file_name.strip())

        clean_name = clean_name.replace(" ", "_")

        return clean_name
    
    def generateFilePath (self, file: UploadFile, project_id : str):
        random_fileName = self.generateRandomString()
        project_path = ProjectController().getProjectPath(project_id=project_id)
        originalName = file.filename
        clean_name = self.get_clean_file_name(
            file_name=originalName
        )

        new_file_name= random_fileName + "_" + clean_name

        new_path = os.path.join(
            project_path,
            new_file_name
        )

        while os.path.exists(new_path):
            random_fileName = self.generateRandomString()
            new_file_name= random_fileName + "_" + clean_name

            new_path = os.path.join(
                project_path,
                new_file_name
            )


        return new_path, new_file_name