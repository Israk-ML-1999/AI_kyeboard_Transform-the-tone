import os
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables from .env file
env_path = Path(__file__).resolve().parent.parent.parent / '.env'
print(f"Loading .env file from: {env_path}")
load_dotenv(dotenv_path=env_path)

# Print environment variables for debugging
api_key = os.getenv("SPORTSRADAR_API_KEY")
base_url = os.getenv("NFL_BASE_URL")
groq_api_key = os.getenv("GROQ_API_KEY")
print(f"API Key loaded: {'*' * 4}{api_key[-4:] if api_key else 'Not found'}")
print(f"Base URL loaded: {base_url}")
print(f"Groq API Key loaded: {'*' * 4}{groq_api_key[-4:] if groq_api_key else 'Not found'}")

# API Configuration
class Settings:
    # API Keys
    GROQ_API_KEY: str = groq_api_key
    
    # API Info for Swagger UI
    API_TITLE: str = "Mood-Based Text Generator"
    API_DESCRIPTION: str = "Generate text based on mood and input prompt using Llama3-70b-8192"
    API_VERSION: str = "1.0.0"
    
    # Model Configuration
    MODEL_NAME: str = "llama3-70b-8192"
    HEADLINE_TEMPERATURE: float = 0.7
    STORY_TEMPERATURE: float = 0.8
    HEADLINE_MAX_TOKENS: int = 50
    STORY_MAX_TOKENS: int = 800

settings = Settings()
