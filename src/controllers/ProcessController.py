from .BaseController import BaseController
from models import ResponseSignal
from fastapi import UploadFile
import os
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import PyMuPDFLoader
from models import ProcessingEnum
from .ProjectController import ProjectController
from langchain_text_splitters import RecursiveCharacterTextSplitter
class ProcessController(BaseController):

    def __init__(self , project_id : str):
        super().__init__()
        
        self.project_id = project_id
        self.project_path = ProjectController().getProjectPath(project_id= project_id)

    def getFileExtension (self, file_id: str):
        return os.path.splitext(file_id)[-1]

    def getFileLoader (self, file_id:str):

        file_ext = self.getFileExtension(file_id=file_id)
        file_path = os.path.join(
            self.project_path,
            file_id
        )
        print(file_ext)
        if file_ext == ProcessingEnum.TXT.value:
            return TextLoader(file_path, encoding = "utf-8")
        
        if file_ext == ProcessingEnum.PDF.value:
            return PyMuPDFLoader(file_path)
        
        return None

    def getFileContent(self , file_id:str):

        loader = self.getFileLoader(file_id=file_id)
        return loader.load()
    
    def processFileContent(self, file_content: list , file_id:str,
                           chunk_size: int = 100 , overlap_size: int = 20 ):
        
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap= overlap_size,
            length_function = len,
        )

        file_content_text = [
            rec.page_content
            for rec in file_content
        ]

        
        file_content_metadata = [
            rec.metadata
            for rec in file_content
        ]

        chunks = text_splitter.create_documents(
            file_content_text,
            metadatas= file_content_metadata
        )

        return chunks