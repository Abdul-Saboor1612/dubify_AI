# test_generate.py (place at root of project)

from app.services.bark_tts import generate_tts

if __name__ == "__main__":
    text = "Hello! This is a test voice generation using Dubify AI."
    voice = "male"  # or "female"
    path = generate_tts(text, voice)
    print(f"✅ Audio saved to: {path}")
