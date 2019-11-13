from gtts import gTTS
import os

txtfile = input("Input the textfile: ")
# Open file
f = open(txtfile, 'r')
# Get the text
text = f.read()
# Close the file
f.close()

genAudio = gTTS(text = text, lang = 'en')

 
outfile = txtfile[:-4] + ".mp3"
genAudio.save(outfile)

#tts.save("test.mp3")

cmd = "cvlc " + outfile
os.system(cmd)


