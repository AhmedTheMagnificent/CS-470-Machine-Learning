import os

APP_TITLE = "✨ A.L.P.H.A. Tutor ✨"
APP_SUBTITLE = "Your Adaptive Learning Personalized Helper Agent"
APP_ICON = "✨"

OLLAMA_MODEL_NAME = "llama3"
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

CHROMA_DB_PATH = "./chroma_db"
CHROMA_COLLECTION_NAME = "alpha_knowledge"
EMBEDDING_MODEL_FALLBACK = "all-MiniLM-L6-v2"

