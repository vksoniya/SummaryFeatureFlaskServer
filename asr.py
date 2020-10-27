from utils.getMeetingInfo import getcurrentMeetingInfo
from utils.chunkAudio import chuckAudio

import speech_recognition as sr
print(sr.__version__)

import os
from os import path

def getFullPath(filename):
    return path.join(path.dirname(path.realpath(__file__)), "data", filename)

UPLOAD_FOLDER = os.path.abspath(os.path.join(rd, "data"))

def convertOpusToWave():
    for x in os.listdir(upload_path):
        if x.endswith('.opus'):
            print(x)
    

def convertAudiotoText(audioPath):
    #convert opus to wav format <- pending 
    r = sr.Recognizer()
    # read the entire audio file
    with sr.AudioFile(getFullPath(audioPath)) as source:
        audio = r.record(source) 

    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        transribedText = r.recognize_google(audio)
        #transribedFileName = os.path.join(os.getcwd(), "data/transcripts", "transText.txt")
        transribedFileName = os.path.join("/home/nvig/Desktop/WILPS/SummarizerFlaskServer/data/transcripts", filename.replace("wav", "txt"))
        print("Google Speech Recognition thinks you said " + transribedText)
        transribedFile = open(transribedFileName, "a")
        transribedFile.writelines(transribedText + "\n")
        transribedFile.close()
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
    return transribedFileName

if __name__ == '__main__':
    filename = "/home/nvig/Desktop/WILPS/SummarizerFlaskServer/SpeechRecognition/tmp/output000000000.wav"
    transribedFileName = convertAudiotoText(filename)
    print(transribedFileName)

#Usage of this function
#convertAudiotoText("male.wav")