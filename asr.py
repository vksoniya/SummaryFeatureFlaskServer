from utils.getMeetingInfo import getcurrentMeetingInfo
from utils.chunkAudio import chuckAudio
from utils.convertToWav import convertToWavFile

import speech_recognition as sr
print(sr.__version__)

import os
from os import path

RECORD_OPUS_FILE = ""
CONF_ID = ""

def extractConfInfo():
    currentMeetingInfo = getcurrentMeetingInfo()
    CONF_ID = currentMeetingInfo['voiceConfID']
    RECORD_OPUS_FILE = currentMeetingInfo['RecordPath']
    # For testing on local
    #CONF_ID = "26471"
    #RECORD_OPUS_FILE = os.path.join(os.getcwd(), "var/freeswitch/meetings/cde145e5c20766d33c81bb492a157a94feb3a0f1-1603617884026-15243890485.opus")
    return CONF_ID, RECORD_OPUS_FILE


def createTranscriptFileName(CONF_ID):
    fName = os.getcwd() + "/MeetingTranscriptData/" + CONF_ID + "_transcript.txt"
    return fName


def getFullPath(filename,CONF_ID):
    return path.join(path.dirname(path.realpath(__file__)), "audio/tmp", CONF_ID, filename)


def convertAudiotoText(audioPath, transcriptFileName):
   
    #get one wav file for now
    for x in sorted(os.listdir(audioPath)):
        if x.endswith('.wav'):
            audioFile = str(x)
            print("Currently Transcribing: " + audioFile)
            r = sr.Recognizer()
            # read the chunked audio file
            with sr.AudioFile(getFullPath(audioFile,CONF_ID)) as source:
                audio = r.record(source) 

            # recognize speech using Google Speech Recognition
            try:
                # for testing purposes, we're just using the default API key
                # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
                # instead of `r.recognize_google(audio)`
                transribedText = r.recognize_google(audio)
                print("Google Speech Recognition thinks you said: " + transribedText)
                transribedFile = open(transcriptFileName, "a")
                transribedFile.writelines(transribedText + ". ")
                transribedFile.close()
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
    return transribedText

if __name__ == '__main__':

    #Get meeting record path
    #get the opus file
    CONF_ID, RECORD_OPUS_FILE = extractConfInfo()
    print("Conf_ID: " + CONF_ID)
    print("Record File:" + str(RECORD_OPUS_FILE))

    #convert to wav and store it in MeetingAudioWav Folder
    wavFileName, wavFilePath = convertToWavFile(RECORD_OPUS_FILE)
    print("Wave File Name: " + wavFileName)
    print("Wave File Path:" + wavFilePath)

    #chunk the file and store it in audio/tmp folder
    tmpAudioPath = chuckAudio(wavFilePath, CONF_ID)

    #create transcrition file in the "MeetingTranscriptData"
    transcriptFileName = createTranscriptFileName(CONF_ID)
    print("Transcript File Name:" + transcriptFileName)

    #transribe each chunck file
    transribedText = convertAudiotoText(tmpAudioPath,transcriptFileName)
    print(transribedText)
    
  
    #Delete the tmp chunked files