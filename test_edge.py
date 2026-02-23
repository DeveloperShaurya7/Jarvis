import asyncio
import edge_tts
import os
import sys

# -----------------------------
# CONFIG
# -----------------------------
DEFAULT_VOICE = "en-AU-NatashaNeural"   # 🔥 Jarvis-style male voice
OUTPUT_FILE = "speech.mp3"


async def speak(text: str, voice: str = DEFAULT_VOICE, filename: str = OUTPUT_FILE):
    """
    Convert text to speech using Microsoft Edge TTS
    """
    if not text.strip():
        print("❌ No text provided")
        return

    try:
        communicate = edge_tts.Communicate(text, voice)
        await communicate.save(filename)

        # Auto-play on Windows
        if sys.platform.startswith("win"):
            os.system(f'start "" "{filename}"')
        else:
            print(f"Audio saved as {filename}")

    except Exception as e:
        print("❌ TTS Error:", e)


def run_tts(text, voice=DEFAULT_VOICE):
    """
    Safe async runner (GUI / background friendly)
    """
    try:
        asyncio.run(speak(text, voice))
    except RuntimeError:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(speak(text, voice))


# -----------------------------
# MAIN
# -----------------------------
if __name__ == "__main__":

    # Take text from command line if provided
    if len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])
    else:
        text = "Hello, I am Jarvis. Systems are online."

    run_tts(
        text=text,
        voice=DEFAULT_VOICE
    )
