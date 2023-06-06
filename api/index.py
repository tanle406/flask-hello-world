from flask import Flask, request
from lib.ask_for_gpt import ask_chatgpt
from lib.text_to_speech import mp3_to_base64

app = Flask(__name__)

@app.route('/', methods=['POST'])
def home():
    data = request.get_json()
    my_text = data['text']
    language = data['language']
    try:
        answer = ask_chatgpt(my_text)
        mp3 = mp3_to_base64(answer, language)
        response = {"answer_text": answer,
                    "answer_base64": mp3}
        return response
    except Exception as e:
        print("Error asking ChatGPT", e)
    

@app.route('/about', methods=['POST'])
def about():
    try:
        data = request.get_json()
        my_text = data['text']
        language = data['language']
        mp3 = mp3_to_base64(my_text, language)
        return mp3
    except Exception as e:
        print("Error asking ChatGPT", e)
        


if __name__ == '__main__':
    app.run()
