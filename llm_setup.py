import os
import streamlit as st
from typing import List, Any
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.llms import Ollama
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.outputs import ChatGeneration, LLMResult
from config import OLLAMA_MODEL_NAME, OLLAMA_BASE_URL, EMBEDDING_MODEL_FALLBACK

@st.cache_resource
def get_llm():
    try:
        llm = Ollama(model_name=OLLAMA_MODEL_NAME, base_url=OLLAMA_BASE_URL)
        st.success(f"Successfully connected to Ollama with model: {OLLAMA_MODEL_NAME} at {OLLAMA_BASE_URL}")
        return llm
    except Exception as e:
        st.error(f"Could not connect to Ollama. Ensure Ollama server is running and '{OLLAMA_MODEL_NAME}' model is pulled. Error: {e}")
        st.warning("Falling back to a Mock LLM for basic functionality. Please set up Ollama for full capabilities.")
        return MockLLM()