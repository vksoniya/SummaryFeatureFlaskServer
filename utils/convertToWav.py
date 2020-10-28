""" Purpose: A Utility script that converts opus audio file to wav audio format
Source Code Creator: Soniya Vijayakumar
Project: WILPS Hamburg University 
Term: Summer 2021
M.Sc. Intelligent Adaptive Systems  """

import os
import subprocess

def convertToWavFile(opusFile):
  
    wavFileName = opusFile[-71:].replace("opus","wav")
    wavFilePath = os.path.join(os.getcwd(), "MeetingAudioWav", wavFileName)
    
    query = "ffmpeg -i " + opusFile + " " + wavFilePath
    response = subprocess.Popen(query, shell=True, stdout=subprocess.PIPE).stdout.read()
    s = str(response).encode('utf-8')

    return wavFileName, wavFilePath