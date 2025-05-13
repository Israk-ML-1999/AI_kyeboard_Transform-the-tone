from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from App.core.config import settings
from App.api.api_routes import router as api_router

# Create FastAPI app
app = FastAPI(
    title=settings.API_TITLE,
    description=settings.API_DESCRIPTION,
    version=settings.API_VERSION
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API router
app.include_router(api_router)

@app.get("/")
async def root():
    return {
        "message": "Welcome to Mood-Based Text Generator API",
        "docs": "/docs",
        "endpoints": {
            "generate": "/api/generate (POST) - Generate text based on mood and prompt"
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)