# app/services/bark_tts.py

import sys
import site
import os

site.addsitedir(os.path.join(os.getcwd(), "venv/lib/python3.11/site-packages"))

from TTS.api import TTS

MODELS = {
    "female": TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False, gpu=False),
    "male": TTS(model_name="tts_models/en/vctk/vits", progress_bar=False, gpu=False)
}

def generate_tts(text: str, voice: str = "female", output_path: str = "output.wav"):
    tts = MODELS.get(voice, MODELS["female"])
    speaker = "p225" if voice == "male" else None

    if speaker:
        tts.tts_to_file(text=text, file_path=output_path, speaker=speaker)
    else:
        tts.tts_to_file(text=text, file_path=output_path)

    return output_path
