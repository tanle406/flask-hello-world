import openai

openai.api_key = "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"
model_engine = "gpt-3.5-turbo" 

def ask_chatgpt(question):
    print("1")
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
        print("2")
        message = response.choices[0]['message']
        return message['content']
    except Exception as e:
        print("ERROR: " + str(e))