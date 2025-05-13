from pydantic import BaseModel, Field
from typing import Literal, Optional

class TextGenerationRequest(BaseModel):
    mood: Literal[
        "happy", "sad", "angry", "excited", "calm", "anxious",
        "romantic", "nostalgic", "hopeful", "mysterious", "humorous",
        "inspiring", "melancholic", "peaceful", "thrilling"
    ]
    prompt: str = Field(..., min_length=1)

class TextGenerationResponse(BaseModel):
    headline: str
    generated_text: str

class ErrorResponse(BaseModel):
    detail: str