import time
import os
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv

import argostranslate.package
import argostranslate.translate

# Load environment variables from .env file
load_dotenv()

app = FastAPI()
start_time = time.time()

# Read environment variables
API_PORT = int(os.getenv("API_PORT", 12448))
LANGUAGES = os.getenv("LANGUAGES", "en:es")

# Parse language pairs
language_pairs = [tuple(pair.split(":")) for pair in LANGUAGES.split(",") if pair]

""" TRANSLATE """
class TranslationRequest(BaseModel):
    text: str
    from_lang: str
    to_lang: str
    
def load_language_packages(language_pairs):
    """
    Function to download and install language packages.
    """
    try:
        argostranslate.package.update_package_index()
        available_packages = argostranslate.package.get_available_packages()
        for from_code, to_code in language_pairs:
            package_to_install = next(filter(lambda x: x.from_code == from_code and x.to_code == to_code, available_packages), None)
            if package_to_install:
                argostranslate.package.install_from_path(package_to_install.download())
        return available_packages
    except Exception as e:
        print(f"Error loading language packages: {e}")
        return []
    
# Load language packages at startup
available_packages = load_language_packages(language_pairs)

""" API REST """
@app.get("/")
def read_root():
    """
    Endpoint to check the uptime of the API.
    """
    current_time = time.time()
    uptime = current_time - start_time
    return {"uptime": uptime}

@app.get("/languages")
def available_languages():
    """
    Endpoint to get available language pairs.
    """
    languages = [{"from": package.from_code, "to": package.to_code} for package in available_packages]
    return {"languages": languages}

@app.post("/translate")
def translate(request: TranslationRequest):
    """
    Endpoint to translate text from one language to another.
    """
    try:
        translated_text = argostranslate.translate.translate(request.text, request.from_lang, request.to_lang)
        return {"translated_text": translated_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
""" START """
if __name__ == "__main__":
    """
    Run the FastAPI application.
    """
    uvicorn.run(app, host="0.0.0.0", port=API_PORT)