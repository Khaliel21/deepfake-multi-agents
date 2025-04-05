import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())
groq_api_key = os.environ['GROQ_API_KEY']
hf_token_api = os.environ['HF_TOKEN_API']
pinecone_api_key = os.environ['PINECONE_API_KEY']
tavily_api_key = os.environ['TAVILY_API_KEY']
langchain_api_key = os.environ["LANGCHAIN_API_KEY"]
os.environ["LANGSMITH_TRACING"] = "true"