Plan
===
[ ] Collect large amounts of voice data and clean it <br>
[ ] Generate a voice model (ideally with Joe Rogan and Morgan Freeman to start) <br>
[x] Add text-to-speech synthesis outputting to an `mp3` file <br>
[ ] Add text-to-speech synthesis using our voice model and output to `mp3` <br>
[x] Add the ability to parse `.txt` files and use TTS to output an mp3 of the text passed in <br>
[ ] Add the ability to parse purely text based `PDF` and store the text <br> 
[ ] Add the ability to parse text based `PDF` with pictures and use the text with TTS <br> 
[ ] Using text based `PDF`, add pics with caption to a separate file, number the pics, and replace the pic with number in the `mp3` output so users can easily reference  
[ ] Add the OCR/ability to parse `PDF` that is image based 
<= might be a longshot, but worth giving it the ol' college try <br>
[ ] Create GUI for the application <br> 
[ ] Add Google Drive integration to facilitate transferring the file between devices <br> 

Setup
===

Pyenv with the latest version of Python
> Pyenv allows you to use multiple versions of Python on your system 
---

Install: <br> 
1. Install pyenv <br>
   ```
   curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash 
   ```
   or (for zsh): 
   ```
   curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | zsh 
   ```
   or (should work on any shell):
   ```
   curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | sh
   ```
2. Show the versions of python that are installed <br>
    ```
    pyenv versions 
    ```
3. Install the most recent version of python, in this case: 3.7.4 <br>
    ```
    pyenv install 3.7.4
    ```
4. Install pyenv virtual environments using pyenv-virtualenv <br>
    ```
    git clone https://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv
    ```
5. Source (restart) your shell <br>
    If you ar using bash: 
    ```
    source ~/.basrc
    ```
    If you are using zsh: 
    ```
    source ~/.zshrc
    ```
    Look up how to do it for your shell if you are using something else <br>
6. Make a directory for your virtualenvs, and change into it <br>
    ```
    cd ~ && \
    mkdir virtual_env && \
    cd virtual_env
    ```
7. Make your virtualenv <br>
    In this case we make a virtualenv using pyenv for version 3.7.4 <br>
    ```
    pyenv virtualenv 3.7.4 wordofmouth
    ```
8. It will show in your versions <br>
    ```
    pyenv versions
    ```
9. You need to be able to use the virtual env <br>
    ```
    pyenv activate wordofmouth
    ```
    Now you should see the virtualenv prepended to the current directiory in the shell listing <br>

10. When you are done, deactivate the virtualenv <br>
    ```
    pyenv deactivate
    ```
Note: <br>
Using `pyenv` and `virtualenv` you are able to install packages in the virtual environment. 
Since you also have Anaconda installed on your computer, you can still use it in the virtualenv
> Ex: `jupyter-lab` will still open the program in the virtualenv)

Pyenv Github: <br>
[Pyenv Github](https://github.com/pyenv/pyenv)

List of pyenv commands: <br>
[Pyenv Commands](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md)

Good guide to pyenv: <br>
[Amaral Lab Guide](https://amaral.northwestern.edu/resources/guides/pyenv-tutorial)

Another Guide to pyenv and virtualenvs: <br>
[Real Python Guide](https://realpython.com/intro-to-pyenv/)

Pyenv-virtualenv Plugin: <br>
[Pyenv-virtualenv Github](https://github.com/pyenv/pyenv-virtualenv)

Epitran
---
Epitran is used to translate text into phonetic form 

Install: <br> 
1. Make sure you are in your virtual environment <br>
    ```
    pyenv activate wordofmouth
    ```
    > Use the name of your virtual environment, in this case it's called word of mouth
2. Install Epitran <br>
    ```
    pip3 install epitran
    ```
Link to Epitran 

[Epitran Pypi Page](https://pypi.org/project/epitran/)

Getting JRE Audio 
---
1. Make sure you import epitran in the notebook first 
2. Go to:
[Joe Rogan Podcasts](http://podcasts.joerogan.net/podcasts/mark-normand)
and find the podcast you would like to use, download it as mp3
3. Go to:
[Subbed Podcasts](https://podscribe.app/feeds/http-joeroganexpjoeroganlibsynprocom-rss/episodes/7798906218684900b35f1eeeaa5c2d64) <br>
This is a transcript of all podcasts, save the text that is associated with segment
4. Cut the audio here:
[Audio Splitter](https://mp3cut.net/) <br>
Download the audio as mp3
5. Finally, convert to wav file at:
[Mp3 to WAV Converter](https://audio.online-convert.com/convert-to-wav)<br>
Download the wav file and save text of it

Useful Libraries
===

Epitran


Resources
====
[Deep Voice: Real-time Neural Text-to-Speech-2017](https://arxiv.org/pdf/1702.07825.pdf)

[Learn How To Build Your Own Speech-to-text Model (Using Python)](https://www.analyticsvidhya.com/blog/2019/07/learn-build-first-speech-to-text-model-python/)

[10 Audio Processing Tasks To Get You Started With Deep Learning Applications (With Case Studies)](https://www.analyticsvidhya.com/blog/2018/01/10-audio-processing-projects-applications/)

[How to use WaveNet](https://towardsdatascience.com/how-wavenet-works-12e2420ef386)

[Paper that the Project is based off of](https://arxiv.org/pdf/1702.07825.pdf)

[Mimic2](https://github.com/MycroftAI/mimic2)

[Smart speaker guide that could be useful](https://respeaker.io/make_a_smart_speaker/)



[List of stuff that could be useful](https://www.findbestopensource.com/product/mozilla-tts)

[Wavenet Encoder](https://github.com/r9y9/wavenet_vocoder)

### This is an amazing resource
[/r/audiomodels](https://www.reddit.com/r/audiomodels/)

### Projects making TTS

[WaveRNN](https://github.com/fatchord/WaveRNN)

[FloWaveNet](https://github.com/ksw0306/FloWaveNet)

# TODO take a look at this. Could be very promising

[Mozilla Text To Speech](https://github.com/mozilla/TTS)

[Related to the above, seen it in use](https://github.com/erogol/TTS_experiments)

[A Test implementation(I think)](https://gist.github.com/erogol/97516ad65b44dbddb8cd694953187c5b)

[Discussion on using pretrained models](https://discourse.mozilla.org/t/any-step-by-step-how-to-documentation-on-synthesizing-with-a-pre-trained-model/45316)

[Discussion on how to use](https://discourse.mozilla.org/t/how-to-use-the-tts-models/42368)

[Use without a GPU](https://discourse.mozilla.org/t/running-tts-on-constrained-hardware-no-gpu/40603)

[Voice Assistant Guide (Implements Mozilla/TTS)](https://blog.rasa.com/how-to-build-a-voice-assistant-with-open-source-rasa-and-mozilla-tools/)

[Lightning Talk on Mozilla/TTS](https://www.youtube.com/watch?v=Tysf_1Myd9g)

[Has link to collab notebook implementing](https://github.com/mozilla/TTS/issues/272)

[Blog by one of the main devs](http://www.erogol.com/gradual-training-with-tacotron-for-faster-convergence/)


This could make our lives a bit easier if we have time at the end
[Speech to text with deep learning](https://github.com/mozilla/DSAlign)


