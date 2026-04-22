# Financial Document Analyzer

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

~TSR