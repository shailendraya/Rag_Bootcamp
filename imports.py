# ============================================================
# Standard Library
# ============================================================

import os
import io
import json
import time
import base64
from pathlib import Path
from datetime import datetime

# ============================================================
# Environment
# ============================================================

from dotenv import load_dotenv
from pydantic import BaseModel
# ============================================================
# Redis
# ============================================================

import redis

# ============================================================
# LangGraph Core
# ============================================================
from langgraph.graph import StateGraph, END


# ============================================================
# LangChain Core
# ============================================================

from langchain_core.documents import Document

from langchain_core.prompts import (
    PromptTemplate,
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
)

from langchain_core.output_parsers import (
    StrOutputParser,
)

from langchain_core.runnables import (
    RunnableLambda,
    RunnableMap,
    RunnableParallel,
    RunnablePassthrough,
    RunnableBranch,
)

# ============================================================
# Chat Models
# ============================================================

from langchain.chat_models import init_chat_model
from openai import OpenAI

# ============================================================
# Embeddings
# ============================================================

from langchain_openai import OpenAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings

# ============================================================
# Document Loaders
# ============================================================

from langchain_community.document_loaders import (
    TextLoader,
    WebBaseLoader,
    CSVLoader,
    PyPDFLoader,
    DirectoryLoader,
    WikipediaLoader,
)

# ============================================================
# Text Splitters
# ============================================================

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter,
    CharacterTextSplitter,
    TokenTextSplitter,
)

from langchain_experimental.text_splitter import (
    SemanticChunker,
)

# ============================================================
# Vector Stores
# ============================================================

from langchain_community.vectorstores import FAISS
# from langchain_chroma import Chroma

# ============================================================
# Retrievers
# ============================================================

from langchain_community.retrievers import BM25Retriever
from langchain_classic.retrievers import EnsembleRetriever

# ============================================================
# Sentence Transformers
# ============================================================

# from sentence_transformers import SentenceTransformer
# from sklearn.metrics.pairwise import cosine_similarity

# ============================================================
# PDF Processing (Multimodal)
# ============================================================

import fitz  # PyMuPDF

# ============================================================
# Image Processing (Multimodal)
# ============================================================

from PIL import Image

# ============================================================
# Deep Learning
# ============================================================

# import torch
# import torchvision

# ============================================================
# Hugging Face - CLIP (Image Embeddings)
# ============================================================

# from transformers import (
#     CLIPModel,
#     CLIPProcessor,
# )

# ============================================================
# Optional Visualization (Useful for tutorials)
# ============================================================

# import matplotlib.pyplot as plt

# ============================================================
# Utility
# ============================================================

from typing import List, Dict, Any

from langchain_community.document_loaders.youtube import YoutubeLoader

from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_core.tools import Tool