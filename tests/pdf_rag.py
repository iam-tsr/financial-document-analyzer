from crewai_tools import PDFSearchTool
import os
from dotenv import load_dotenv
load_dotenv()
from chromadb.config import Settings

tool = PDFSearchTool()

tool = PDFSearchTool(
    pdf='data/TSLA-Q2-2025-Update.pdf',
    config={
        "embedding_model": {
            # Supported providers: "openai", "azure", "google-generativeai", "google-vertex",
            # "voyageai", "cohere", "huggingface", "jina", "sentence-transformer",
            # "text2vec", "ollama", "openclip", "instructor", "onnx", "roboflow", "watsonx", "custom"
            "provider": "google-generativeai",  # or: "google-generativeai", "cohere", "ollama", ...
            "config": {
                # Model identifier for the chosen provider. "model" will be auto-mapped to "model_name" internally.
                # "model": "gemini-embedding-001",
                # "GEMINI_API_KEY": os.getenv("GEMINI_API_KEY"),  # Example for Google Generative AI. Use provider-specific env vars or pass api_key directly.
                # Optional: API key. If omitted, the tool will use provider-specific env vars
                # (e.g., OPENAI_API_KEY or EMBEDDINGS_OPENAI_API_KEY for OpenAI).
                # "api_key": "sk-...",

                # Provider-specific examples:
                # --- Google Generative AI ---
                # (Set provider="google-generativeai" above)
                "model_name": "gemini-embedding-001",
                "task_type": "RETRIEVAL_DOCUMENT",
                "title": "Embeddings",

                # --- Cohere ---
                # (Set provider="cohere" above)
                # "model": "embed-english-v3.0",

                # --- Ollama (local) ---
                # (Set provider="ollama" above)
                # "model": "nomic-embed-text",
            },
        },
        "vectordb": {
                    "provider": "chromadb",  # or "qdrant"
                    "config": {
                        # For ChromaDB: pass "settings" (chromadb.config.Settings) or rely on defaults.
                        # Example (uncomment and import):
                        "settings": Settings(
                            persist_directory="/content/chroma",
                            allow_reset=True,
                            is_persistent=True,
                        ),

                        # For Qdrant: pass "vectors_config" (qdrant_client.models.VectorParams).
                        # Example (uncomment and import):
                        # from qdrant_client.models import VectorParams, Distance
                        # "vectors_config": VectorParams(size=384, distance=Distance.COSINE),

                        # Note: collection name is controlled by the tool (default: "rag_tool_collection"), not set here.
                    }
        },
    }
)