#!/usr/bin/env python3

from tkinter import Tk, Button, filedialog
from pydub import AudioSegment
from dotenv import load_dotenv
import openai
import os

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    raise ValueError("API key not found. Make sure the OPENAI_API_KEY environment variable is set.")

openai.api_key = api_key

window = Tk()
window.title("Transcribe and Summarize Your Audio Files")

selected_file_path = None
transcribed = False
summarized_text = None

def browse_file():
    global selected_file_path
    global transcribed

    filetypes = [
        ("Audio Files", "*.m4a;*.wav;*.mp3"),
        ("M4A Files", "*.m4a"),
        ("WAV Files", "*.wav"),
        ("MP3 Files", "*.mp3")
    ]

    selected_file_path = filedialog.askopenfilename(filetypes=filetypes)


    if selected_file_path:
        transcribed = False
        transcribe_button.config(state="normal")
        transcribe_button.config(text="Transcribe")
    else:
        transcribe_button.config(state="disabled")
    
    download_button.config(state="disabled")

def transcribe():
    global transcribed
    global summarized_text

    transcribed = True
        
    audio_file= open(selected_file_path, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)['text']
    summarized_text = generate_summarized_text(transcript)


    transcribe_button.config(text="Transcription Complete")
    transcribe_button.config(state="disabled")
    download_button.config(state="normal")

def download_notes():
    
    notes_file_name = os.path.splitext(selected_file_path)[0] + " Notes"
    default_filename = os.path.basename(notes_file_name)
        
    save_path = filedialog.asksaveasfilename(defaultextension=".md", initialfile=default_filename)

    if save_path:
        with open(save_path, 'w') as f: f.write(summarized_text)
        else: print("No save location selected!")

def generate_summarized_text(transcript):
    
    user_prompt = read_prompt_from_file("user_prompt.txt")
    example_prompt = read_prompt_from_file("example_prompt.txt")

    user_prompt = f"{user_prompt.replace('{{transcript}}', transcript)}"
    system_prompt = example_prompt

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": user_prompt},
            {"role": "system", "content": system_prompt}],
        max_tokens=2000,
        n=1,
        stop=None,
        temperature=0.2
    )

    return response['choices'][0]['message']['content']

def convert_audio_to_text(audio):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=audio,
        max_tokens=200,
        n=1,
        stop=None,
        temperature=0.2
    )
    return response.choices[0].text.strip()

def read_prompt_from_file(file_name):
    with open(file_name, 'r') as f:
        prompt = f.read().strip()
    return prompt

browse_button = Button(window, text="Upload Audio File", command=browse_file)
browse_button.pack()

transcribe_button = Button(window, text="Transcribe", command=transcribe, state="disabled")
transcribe_button.pack()

download_button = Button(window, text="Download Notes", command=download_notes, state="disabled")
download_button.pack()

window.mainloop()
