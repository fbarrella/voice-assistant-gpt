from gtts import gTTS

import speech_recognition as sr
import soundfile as sf
import io
import winsound
import os
import openai
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ.get("API_KEY"),
)

model_engine = os.environ.get("MODEL_ENGINE", "deepseek/deepseek-r1-0528:free")
assistant_name = os.environ.get("CALLOUT", "alice")
end_assistant_command = os.environ.get("DISMISSAL", "pode parar")

def print_phrase(phrase):
    print("Q:", phrase)

def fetch_response(voice_input):
    response = client.chat.completions.create(
        extra_body={},
        extra_headers={},
        model=model_engine,
        messages=[
            {
                "role": "user",
                "content": f"Responda de forma curta e pratica: {voice_input}",
            }
        ],
    )

    return response.choices[0].message.content

def say_loud(phrase):
    # Generate an audio file from the user text input using gTTS
    tts = gTTS(text=phrase, lang='pt-br')
    audio_file = io.BytesIO()
    tts.write_to_fp(audio_file)
    audio_file.seek(0)

    # Create a temporary audio file using soundfile
    audio_file_path = "temp_audio.wav"
    with sf.SoundFile(audio_file_path, mode="w", samplerate=28000, channels=1) as file:
        audio_data, _ = sf.read(io.BytesIO(audio_file.read()), dtype="float32")
        file.write(audio_data)

    # Play the audio file using winsound
    winsound.PlaySound(audio_file_path, winsound.SND_FILENAME)

    # Remove the temporary audio file
    os.remove(audio_file_path)

# obtain audio from the microphone
r = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as source:
            print("Waiting for command...")
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)

        # recognize speech using Google Speech Recognition
        command = r.recognize_google(audio,language='pt-BR')

        # check if the command defined on the "assistant_name" variable is said
        if assistant_name in command.lower():
            
            # extract the phrase that comes after your command of choice
            phrase = command.lower().split(assistant_name, 1)[1].strip()

            # execute the function with the phrase as argument
            print_phrase(phrase)

            if phrase == end_assistant_command:
                break

            answer = fetch_response(phrase)

            print('A:', answer.encode("utf-8"))

            say_loud(answer)
    except sr.UnknownValueError:
        print("Nothing said or done.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
