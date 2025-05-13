from fastapi import APIRouter, HTTPException
from groq import Groq
from App.core.config import settings
from App.models.schemas import TextGenerationRequest, TextGenerationResponse
import re

router = APIRouter(prefix="/api", tags=["Text Generation"])

# Initialize Groq client
client = Groq(api_key=settings.GROQ_API_KEY)

def count_words(text: str) -> int:
    """Count the number of words in a text."""
    return len(re.findall(r'\w+', text))

def extract_word_count(text: str) -> int:
    """Extract word count from text if mentioned."""
    # Look for patterns like "within X words", "in X words", etc.
    patterns = [
        r'within\s+(\d+)\s+words?',
        r'in\s+(\d+)\s+words?',
        r'(\d+)\s+words?',
        r'word\s+count:\s*(\d+)',
        r'limit:\s*(\d+)\s+words?'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, text.lower())
        if match:
            return int(match.group(1))
    return None

@router.post("/generate", response_model=TextGenerationResponse)
async def generate_text(request: TextGenerationRequest):
    try:
        # Extract word count from prompt if mentioned
        word_count = extract_word_count(request.prompt)
        
        # Generate headline based on mood and prompt
        headline_prompt = f"""You are an expert headline writer. Create a compelling, emotional headline for a {request.mood} story.
        Context: {request.prompt}
        Requirements:
        - Keep it under 10 words
        - Make it emotionally engaging
        - Match the {request.mood} mood
        - Be creative and unique"""

        headline_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": headline_prompt}],
            model=settings.MODEL_NAME,
            temperature=settings.HEADLINE_TEMPERATURE,
            max_tokens=settings.HEADLINE_MAX_TOKENS
        )
        headline = headline_completion.choices[0].message.content.strip()

        # Transform the text based on mood
        word_count_instruction = f"Transform the text into exactly {word_count} words." if word_count else "Transform the text while maintaining its original length."
        
        transform_prompt = f"""You are a master of emotional writing. Transform the following text into a {request.mood} tone while keeping the same meaning and context.
        
        Original Text: "{request.prompt}"
        
        Requirements:
        - Maintain the same core message and facts
        - Transform the tone to be {request.mood}
        - Use appropriate emotional language and expressions
        - {word_count_instruction}
        - Make it sound natural and authentic
        - Preserve any specific details or names mentioned
        
        Write the transformed text:"""
        
        text_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": transform_prompt}],
            model=settings.MODEL_NAME,
            temperature=settings.STORY_TEMPERATURE,
            max_tokens=settings.STORY_MAX_TOKENS
        )
        transformed_text = text_completion.choices[0].message.content.strip()

        # If word count was specified and the generated text is too long, trim it
        if word_count:
            words = transformed_text.split()
            if len(words) > word_count:
                transformed_text = ' '.join(words[:word_count])

        return TextGenerationResponse(
            headline=headline,
            generated_text=transformed_text
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))