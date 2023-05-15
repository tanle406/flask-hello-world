from gtts import gTTS
import os
import base64

def mp3_to_base64(mytext, language):

    audio = gTTS(text=mytext, lang=language, slow=False)
    print(1)
    audio.save("example.mp3")
    print(2)
    with open("example.mp3", "rb") as mp3_file:
        encoded_string = base64.b64encode(mp3_file.read())
    print(3)
    os.remove("example.mp3")
    print(4)
    return encoded_string
