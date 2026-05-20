from fastapi import FastAPI
from pydantic import BaseModel
import hashlib

app = FastAPI()


class TextRequest(BaseModel):
    text: str


@app.get("/")
def home():
    return {
        "message": "Welcome to GitHub Copilot Lab - Developed by Venkata Ramana"
    }


def generate(text: str):
    """
    Generate MD5 checksum for the given text.
    """
    return hashlib.md5(text.encode()).hexdigest()


@app.post("/checksum")
def create_checksum(request: TextRequest):
    """
    Accepts text and returns a checksum generated using the generate() function.
    """
    checksum = generate(request.text)
    return {
        "input_text": request.text,
        "checksum": checksum
    }
