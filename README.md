# Voicebot 

A real-time **voice AI assistant** built with [LiveKit](https://livekit.io/), [Google Gemini](https://ai.google.dev/), [Deepgram](https://deepgram.com/), and [Cartesia](https://cartesia.ai/) for **speech-to-text (STT)**, **large language model (LLM)**, and **text-to-speech (TTS)**.

---

##  Features

* 🎤 Real-time voice interaction
* 🗣️ Speech-to-Text (Deepgram / Google STT)
* 🤖 Conversational AI (Google Gemini LLM)
* 🔊 Text-to-Speech (Cartesia)
* 📡 Powered by LiveKit for low-latency streaming

---

## Installation

1. Clone this repository:
   `git clone https://github.com/YOUR_USERNAME/Voicebot.git && cd Voicebot`

2. Create and activate a virtual environment (optional but recommended):

   * Linux/Mac: `python -m venv venv && source venv/bin/activate`
   * Windows: `python -m venv venv && venv\Scripts\activate`



3. Create a `.env` file in the project root with the following content:

```
DEEPGRAM_API_KEY=your_deepgram_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
CARTESIA_API_KEY=your_cartesia_api_key_here
LIVEKIT_API_KEY=your_livekit_api_key_here
LIVEKIT_API_SECRET=your_livekit_secret_here
LIVEKIT_URL=wss://your-livekit-url
```


##  Usage

Start the application with:
`python app.py dev`

This will connect your bot to LiveKit and start listening/responding in real time.

---

## 📜 License

This project is licensed under the **MIT License**.

---

