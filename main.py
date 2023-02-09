import os
import openai
import speech_recognition as sr
from gtts import gTTS
import time

# Initialize the recognizer
r = sr.Recognizer()
openai.api_key = 'your api key'
start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

while True:
  with sr.Microphone() as source:
      # read the audio data from the default microphone
      print("Recording...")
      audio_data = r.record(source, duration=6)
      print("Recognizing...")
      prompt = r.recognize_google(audio_data)

  if prompt == 'stop':
    break
  else:
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt= prompt,
      temperature=0.9,
      max_tokens=150,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0.6,
      stop=[" Human:", " AI:"]
    )

    bot_res = response['choices'][0]['text']
    print(bot_res)

    audio = gTTS(text=bot_res, lang="en", slow=False)
    audio.save("response.mp3")
    os.system("start response.mp3")
    time.sleep(30)