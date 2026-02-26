from crewai.tools import BaseTool
from crewai_tools import PDFSearchTool
from typing import Type
from pydantic import BaseModel, Field
from chromadb.config import Settings
from crewai_tools import SerperDevTool
from langchain_community.document_loaders import PyPDFLoader

## Creating search tool
search_tool = SerperDevTool()

## Creating custom pdf reader tool
class FinancialDocumentTool(BaseTool):
    name: str = "Financial Document Reader"
    description: str = (
        "Tool to read data from a pdf file from a path"
    )
    
    def _run(self, path: str):
        """Tool to read data from a pdf file from a path

        Args:
            path (str): Path of the pdf file.

        Returns:
            str: Full Financial Document file
        """
        
        docs = PyPDFLoader(file_path=path).load()

        full_report = ""
        for data in docs:
            # Clean and format the financial document data
            content = data.page_content
            
            # Remove extra whitespaces and format properly
            while "\n\n" in content:
                content = content.replace("\n\n", "\n")
                
            full_report += content + "\n"
            
        return full_report