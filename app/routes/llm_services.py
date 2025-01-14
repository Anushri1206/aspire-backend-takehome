from pathlib import Path
from fastapi import APIRouter, Request, Response


router = APIRouter()

BASE_PATH = Path(__file__).parent.resolve()

# Add your Route here