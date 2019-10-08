from gtts import gTTS
import os
# tts = gTTS(text="Chris! Chris! I need a perc30 me boy. Help me! Danny! Bliss!", lang = 'en')
#tts = gTTS(text="Creighton hi you are a bitch!", lang = 'en')

# Open file
f = open("test.txt", 'r')
# Get the text
text = f.read()
# Close the file
f.close()

genAudio1 = gTTS(text = text, lang = 'en')
genAudio2 = gTTS(text = text, lang = 'en', slow=True)

 
genAudio1.save('testv2fast.mp3')
genAudio2.save('testv2slow.mp3')

#tts.save("test.mp3")

os.system("vlc testv2fast.mp3")

os.system("gtts-cli 'Break it down now yall!' | vlc - ")

os.system("vlc testv2slow.mp3")
