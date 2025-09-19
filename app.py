import os
from dotenv import load_dotenv
from livekit import agents
from livekit.agents import AgentSession, Agent, RoomInputOptions
from livekit.plugins import (
    openai,
    cartesia,
    deepgram,
    google,
    noise_cancellation,
    silero,
)

# Load .env file (force override to always use latest values)
load_dotenv(override=True)

# Print loaded keys to confirm (optional but useful for debugging)
print("🔊 Deepgram:", os.getenv("DEEPGRAM_API_KEY"))
print("🤖 Google:", os.getenv("GEMINI_API_KEY"))
print("🎵 Cartesia:", os.getenv("CARTESIA_API_KEY"))
print("📡 LiveKit Key:", os.getenv("LIVEKIT_API_KEY"))
print("🔑 LiveKit Secret:", os.getenv("LIVEKIT_API_SECRET"))
print("🌐 LiveKit URL:", os.getenv("LIVEKIT_URL"))

class Assistant(Agent):
    def __init__(self) -> None:  
        super().__init__(instructions="You are a helpful voice AI assistant.")  

async def entrypoint(ctx: agents.JobContext):
    session = AgentSession(
        stt=deepgram.STT(model="nova-3", language="en"),  # ✅ Deepgram handles STT
        llm=google.LLM(model="gemini-2.5-flash"),        # ✅ Google for LLM
        tts=cartesia.TTS(model="sonic-2", voice="f786b574-daa5-4673-aa0c-cbe3e8534c02"),
        vad=silero.VAD.load(),
    )


    await session.start(
        room=ctx.room,
        agent=Assistant(),
        room_input_options=RoomInputOptions(
        noise_cancellation=noise_cancellation.BVC(),
        ),
    )

    await session.generate_reply(
        instructions="Greet the user and offer your assistance."
    )

if __name__ == "__main__": 
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))
