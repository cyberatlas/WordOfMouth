# imports
import pdftotext
import os
import argparse

# NOTE: must have WaveRNN and its deps, must have SOX installed
# TODO clean up by letting it take args

# Takes input stream and writes one line at a time to sentences.txt
def make_sentences(textin):
    try:
        # Opens the file to write, overrites if exists and creates if it doesn't
        # By using with statements files are automatically closed for us
        with open("WaveRNN/sentences.txt", "w+") as sent:
            for line in textin:
                sent.write(line)
    except IOError as e:
        print("Could not open/create sentences.txt")
        print(e)
        exit(1)


def main():
    # Parse the args for file location
    parser = argparse.ArgumentParser(description = "Reads in a pdf or txt file, outputs an audio file of it being read")
    parser.add_argument('file', help = "The file you would like to input")
    args = parser.parse_args()
    # Saving the file location
    file = args.file
    
    # TODO might need to make this more robust
    # Check the extension of the file and save the texxt
    if file[-3:] == 'pdf':
        try:
            with open(file, "rb") as file_in:
                text = pdftotext.PDF(file_in)
                
            print("Number of pages: ", len(text))
           # print("\n\n".join(pdf))
        except IOError as e:
            print("Could not open the file!")
            print(e)
            exit(1)
    elif file[-3:] == 'txt':
        #f = open(file, 'r')
        with open(file, 'r') as file_in:
            text = file_in.read()
    else:
        print("Input a txt or pdf file")
        exit(1)

    make_sentences(text)

    """
    # Delete sentences.txt if it already exists
    if os.path.exists("/WaveRNN/sentences.txt"):
        os.remove("WaveRNN/sentences.txt")
    """

    # Delete the quick_start dir if exists, does not do anything if it does not
    os.system("rm -rf WaveRNN/quick_start/")
    

    working_dir = os.getcwd()
    tmp_dir = working_dir + "/WaveRNN" 
    os.chdir(tmp_dir)
    assert(os.getcwd() == tmp_dir), "Issues changing into WaveRNN directory"

    # Run wavrnn
    #os.system("python WaveRNN/quick_start.py")
    try:
        os.system("python quick_start.py")
    except:
        print("isues with wavernn")
        exit(1)

    os.chdir(working_dir)
    assert(os.getcwd() == working_dir), "Issues changing from WaveRNN dir to working dir"

    out_file = file[:-4] + ".wav"
    
    # Concatenate the wav files and save as the output file
    concat_cmd = "sox WaveRNN/quick_start/*.wav '" + out_file + "'"
    os.system(concat_cmd)
    
    # TODO output the file to the user
    os.system("ls")
    print("Your generated audio is ", out_file)


# TODO could add ability to save as mp3
# TODO add error checking around the os.sys]tem stuff
# TODO Add ability to do page range
# TODO add ability to preview page first

main()
