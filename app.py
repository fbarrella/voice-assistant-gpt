from gtts import gTTS

import speech_recognition as sr
import soundfile as sf
import io
import winsound
import os
import openai

openai.api_key = '[OPENAI-TOKEN]'
model_engine = 'gpt-3.5-turbo'
assistant_name = "[ASSISTANT-CALLOUT]"
end_assistant_command = "[ASSISTANT-DISMISS]"

def print_phrase(phrase):
    print("Q:", phrase)

def fetch_response(voice_input):
    response = openai.ChatCompletion.create(
        model=model_engine,
        messages=[
            {
                "role": "user",
                "content": voice_input
            }
        ],
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7
    )

    return response.get('choices', {})[0].get('message', {}).get('content', 'Não foi possivel encontrar nenhuma resposta.')

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

        # check if the word "arnold" is said
        if assistant_name in command.lower():
            
            # extract the phrase that comes after the word "arnold"
            phrase = command.lower().split(assistant_name, 1)[1].strip()

            # execute the function with the phrase as argument
            print_phrase(phrase)

            if phrase == end_assistant_command:
                break

            answer = fetch_response(phrase)

            print('A:', answer)

            say_loud(answer)
    except sr.UnknownValueError:
        print("Nothing said or done.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
