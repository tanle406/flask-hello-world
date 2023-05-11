from flask import Flask, request
from lib.ask_for_gpt import ask_chatgpt
from lib.text_to_speech import mp3_to_base64

app = Flask(__name__)

@app.route('/')
def home():
    data = request.get_json()
    my_text = data['text']
    language = data['language']
    try:
        print("Welcome")
        answer = ask_chatgpt(my_text)
        mp3 = mp3_to_base64(answer, language)
        return mp3
    except Exception as e:
        print("Error asking ChatGPT", e)
    

@app.route('/about')
def about():
    return 'About'