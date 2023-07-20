from fastapi import FastAPI, Depends
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from .routes import router
from .models import get_db
import logging
app = FastAPI(
     title="Project Title",
     description="API for Project",
     version="0.0.1"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

# # Configure logging
# logging.basicConfig(level=logging.INFO)

@app.get('/')
async def root():
  return {
    'success': True,
    'message': 'Hello World!',
    'data': None
  }
  
app.include_router(router)
