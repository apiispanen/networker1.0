# networker
Tests with Open AI to improve networking

## Basic Summary
OpenAI has impressed the world with ChatGPT. It is the combination of openai's text prompting algorithm, combined with Google's Speech to Text.

### TO RUN: Simply run the "app.py" file, and the GUI will appear. Push to talk, to ask the AI questions (be sure to config your default mid to avoid issues.) 

Py Scripts: 
- App
  - Central Application, made using TKinter for a GUI
- Prompt
  - OpenAI's API script, pulling the text data and submitting a response.
- STT (Speech to text)
  - Using Google Cloud's speech to text API, voice data is recognized as text for input in app.py. 
- TTS (Text to Speech)
  - Using Google Cloud's text to speech API, we can gather text and output speech here.
- conversation.js
  - Holds prior conversation data.

Autorization Scripts (not added to GH):
- creds.py - holds API Keys in a Python format
- google.json - holds google authorization payload