# imports
import pdftotext
import os
import argparse

# NOTE: must have WaveRNN and its deps, must have SOX installed
# TODO clean up by letting it take args

# Parse the args for file location
parser = argparse.ArgumentParser(description = "Reads in a pdf or txt file, outputs an audio file of it being read")
parser.add_argument('file', help = "The file you would like to input")
args = parser.parse_args()
file = args.file

# TODO might need to make this more robust
# Check the extension of the file and save the texxt
if file[-3:] == 'pdf':
    try:
        with open(file, "rb") as text:
            pdf = pdftotext.PDF(text)

        print("Number of pages: ", len(pdf))
        print("\n\n".join(pdf))
    except IOError:
        print("Could not open the file!")

    print("WIP")
elif file[-3:] == 'txt':
    f = open(file, 'r')
    text = f.read()
    print(text)
    f.close()

    print("wip")
else:
    print("Input a txt or pdf file")
    exit(1)


# Delete sentences.txt if it already exists
if os.path.exists("sentences.txt"):
    os.remove("sentences.txt")

# Delete the quick_start dir if exists, does not do anything if it does not
os.system("rm -rf quick_start/")

# TODO Save our file 1 line at a time to sentences.txt

# Run wavrnn
os.system("python Wavernn/quick_start.py")

out_file = file + ".wav"

# Concatenate the wav files and save as the output file
concat_cmd = "sox WaveRNN/quick_start/*wav " + out_file
os.system(concat_cmd)

# TODO output the file to the user
os.system("ls")
print("Your generated audio is ", out_file)


# TODO could add ability to save as mp3
# TODO add error checking around the os.system stuff
