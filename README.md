# Mood-Based Text Generator

A FastAPI application that generates text based on mood and input prompts using the Groq LLM API.

## Features

- Generate text based on different moods (happy, sad, angry, excited, calm, anxious)
- Two-step generation process:
  1. Generates an engaging headline based on the mood and prompt
  2. Generates a full story matching the mood and context
- RESTful API with Swagger documentation
- Environment variable configuration

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory with your Groq API key:
```
GROQ_API_KEY=your_groq_api_key_here
```

## Running the Application

1. Start the server:
```bash
python main.py
```

2. Access the API:
- API Documentation: http://localhost:8000/docs
- API Root: http://localhost:8000

## API Usage

### Generate Text

**Endpoint:** `POST /generate`

**Request Body:**
```json
{
    "mood": "happy",  // One of: happy, sad, angry, excited, calm, anxious
    "prompt": "Your input text here"
}
```

**Response:**
```json
{
    "headline": "Generated headline",
    "generated_text": "Generated story text"
}
```

## Example

```python
import requests

response = requests.post(
    "http://localhost:8000/generate",
    json={
        "mood": "happy",
        "prompt": "A day at the beach"
    }
)

print(response.json())
```

## Environment Variables

- `GROQ_API_KEY`: Your Groq API key for accessing the LLM service
