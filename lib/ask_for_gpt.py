import openai
import base64



key_encode = "c2stRmJvbnVBNkZtM043OE0xRUx2UmlUM0JsYmtGSlFlbmhDTGpaV1F5d3FYS0dHcUxZdGFu"

model_engine = "gpt-3.5-turbo" 

def decode_key():

    decoded_bytes = base64.b64decode(key_encode)
    decoded_string = decoded_bytes.decode("utf-8")

    return decoded_string[:-3]

openai.api_key = decode_key()

def ask_chatgpt(question):
    try:
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            n=1,
            messages=[
                {"role": "system", "content": \
                    "You are a helpful assistant with exciting, \
                    interesting things to say."},
                {"role": "user", "content": question},
            ])
        message = response.choices[0]['message']
        return message['content']
    except Exception as e:
        print("ERROR: " + str(e))
