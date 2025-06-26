from fastapi import APIRouter, Form
from app.services.bark_tts import generate_tts

router = APIRouter()

@router.post("/generate")
async def generate(
    text: str = Form(...),
    voice: str = Form("female")
):
    try:
        wav_path = generate_tts(text, voice)
        return {"message": f"Audio generated successfully and saved to {wav_path}"}
    except Exception as e:
        return {"error": str(e)}
