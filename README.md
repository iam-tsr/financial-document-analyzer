# Financial Document Analyzer - Debug Assignment

## Project Overview
A comprehensive financial document analysis system that processes corporate reports, financial statements, and investment documents using AI-powered analysis agents.

## 🚀 Getting Started

### Isolated Environment
```bash
python -m venv .venv

# activate environment
source .venv/bin/activate
```

### Install Required Libraries
```bash
pip install -r requirement.txt
```

### Environment variable
```bash
cp .env.example .env
```
Place your API key as mentioned. Don't know where to find API key? [Gemini API Key](https://aistudio.google.com/api-keys) | [Serper API Key](https://serper.dev/api-keys) | [MongoDB](https://cloud.mongodb.com)

### Run Program
```bash
python main.py
```

### Test System
You can use any API testing platform (i.e. Postman).

Configuration:
```
Method - POST

URL - http://0.0.0.0:8000

Body -> form-data

Change Key type to file and give input as "file" and in value select any your PDF file
```

### Sample Document
The system analyzes financial documents like Tesla's Q2 2025 financial update.

**To add Tesla's financial document:**
1. Download the Tesla Q2 2025 update from: https://www.tesla.com/sites/default/files/downloads/TSLA-Q2-2025-Update.pdf.
2. Save it as `data/sample.pdf` in the project directory.
3. Or upload any financial PDF through the API endpoint.

## 🐛 Bug Hunting

- **Infected Prompt:** All the system and tool prompts were misleading, which I improved for better model generalization and reasoning.
- **Wrong Library Initialization:** I go through CrewAI documentation and verify all the library implementations.
- **Fixed Custom Tools:** Since we've implemented personalized tools through the subclassing technique. Because of this, we need to inherit from BaseTool and define the necessary attributes, including the `name` (Name of tool), `description` (What this tool does), & `args_schema` for input validation, and the `_run` method.
- **File Processing:** Used Langchain's `PyPDFLoader` for extracting text from PDF and feeding it to the `financial_analyst` agent.
- **Parameter Tuning:** Updated the parameter of `max_iter` to 5 to allow the agent to retry if tool use fails and removed `max_rpm` to avoid strict rate limiting issues.
- **LLM Config:** Used `gemini-2.5-flash-lite` with `temperature=0.7` (increase word randomness) and `max_output_tokens=4096` (saves token and cost).
- **Google Search:** Used Google Serper Search for URL references that are related to financial topics.

## 🌟 Introduced Features

- **Database Integration:** I've used MongoDB, where it is storing - PDF file, Query, Analysis result.
- **Improved Requirement File:** Removed all the unused packages.
- **Codebase:** Improved codebase structure, making it clean and readable, which I've pushed in [v2 branch](https://github.com/iam-tsr/financial-document-analyzer/tree/v2).


~TSR