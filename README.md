# GPT Based Audio Chatbot

This bot is based on the `text-davinci-0031` model from OpenAI.

### Working steps:

- Captures and recognizes audio (listening phase).
- Make an API request to OpenAI and get the response (processing phase).
- Create an audio file from the text (output phase).

### Libraries required:
- openai
- speech_recognition
- gtts

Installing commands:
- pip install openai
- pip install SpeechRecognition
- pip install gTTS

NB: You can vary the sleep time to adjust the conversation pace.