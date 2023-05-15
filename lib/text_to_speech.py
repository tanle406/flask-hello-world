from gtts import gTTS
import os
from io import BytesIO
import base64

def mp3_to_base64(mytext, language):

    audio = gTTS(text=mytext, lang=language, slow=False)
    print(1)

    mp3_buffer = BytesIO()
    audio.write_to_fp(mp3_buffer)

    base64_audio = base64.b64encode(mp3_buffer.getvalue()).decode('utf-8')

    return base64_audio
