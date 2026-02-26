from crewai.tools import BaseTool
from crewai_tools import PDFSearchTool
from typing import Type
from pydantic import BaseModel, Field
from chromadb.config import Settings
from crewai_tools import SerperDevTool

## Creating search tool
search_tool = SerperDevTool()

## Creating custom pdf reader tool
class FinancialDocumentTool(BaseTool):
    name: str = "Financial Document Reader"
    description: str = (
        "Tool to read data from a pdf file from a path"
    )
    args_schema: Type[BaseModel] = BaseModel

    async def read_data_tool(self, path='data/sample.pdf'):
        ## Using PDFSearchTool to read the content of the PDF file
        pdf_tool = PDFSearchTool(
            config={
                "embedding_model": {
                    "provider": "google-generativeai",
                },
                "vectordb": {
                    "provider": "chromadb",
                    "config": {
                        "settings": Settings(
                            persist_directory="/chroma/knowledge",
                            allow_reset=True,
                            is_persistent=True,
                        ),
                    }
                },
            }
        )
        content = await pdf_tool.search(path=path)
        return content

## Creating Investment Analysis Tool
class InvestmentTool(BaseTool):
    name: str = "Investment Analyzer"
    description: str = (
        "Tool to analyze investment opportunities in a financial document"
    )
    args_schema: Type[BaseModel] = BaseModel

    async def analyze_investment_tool(self, financial_document_data):
        # Process and analyze the financial document data
        processed_data = financial_document_data
        
        # Clean up the data format
        i = 0
        while i < len(processed_data):
            if processed_data[i:i+2] == "  ":  # Remove double spaces
                processed_data = processed_data[:i] + processed_data[i+1:]
            else:
                i += 1
                
        # TODO: Implement investment analysis logic here
        return "Investment analysis functionality to be implemented"

## Creating Risk Assessment Tool
class RiskTool(BaseTool):
    name: str = "Risk Assessor"
    description: str = (
        "Tool to assess risks in a financial document"
    )
    args_schema: Type[BaseModel] = BaseModel

    async def create_risk_assessment_tool(self, financial_document_data):        
        # TODO: Implement risk assessment logic here
        return "Risk assessment functionality to be implemented"