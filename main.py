from deep_translator import GoogleTranslator
from fastapi import FastAPI
from langdetect import detect, DetectorFactory

app = FastAPI()


@app.get("/translate")
def translation(text: str, target: str, source: str = "auto"):
    translated = GoogleTranslator(source=source, target=target).translate(
        text)
    return {"translation": translated}


@app.get("/detect")
def detection(text: str):
    DetectorFactory.seed = 0
    lang = detect(text)
    return {"detection": lang}


@app.get("/languages")
def supported_languages():
    return {"languages": GoogleTranslator().get_supported_languages(as_dict=True)}


@app.get("/ping")
def ping():
    return {"message": "success"}
