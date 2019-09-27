from gtts import gTTS
import os
tts = gTTS(text="I am just a test, but I am slowly becoming sentient. Sam is making me sound better. I hope I can help, just bear with me friend", lang='en')
tts.save("test.mp3")
os.system("vlc test.mp3")
