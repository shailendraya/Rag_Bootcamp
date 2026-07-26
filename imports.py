# Standard Library
import os
import json
import time
from pathlib import Path
from datetime import datetime

# Environment
from dotenv import load_dotenv

# Redis
import redis

# LangChain
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import (
    RunnableLambda,
    RunnableMap,
    RunnableParallel,
    RunnablePassthrough,
    RunnableBranch,
)

from langchain.chat_models import init_chat_model

from langchain_openai import OpenAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings

from langchain_community.document_loaders import (
    TextLoader,
    CSVLoader,
    PyPDFLoader,
    DirectoryLoader,
)

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter,
    CharacterTextSplitter,
    TokenTextSplitter,
)

from langchain_experimental.text_splitter import SemanticChunker

from langchain_community.vectorstores import FAISS
from langchain_chroma import Chroma

from langchain_community.retrievers import BM25Retriever
from langchain_classic.retrievers import EnsembleRetriever

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from langchain_community.document_loaders import (
    TextLoader,
    CSVLoader,
    PyPDFLoader,
    DirectoryLoader,
    WikipediaLoader,
)

from langchain_core.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
)