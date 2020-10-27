import os
import subprocess

def convertToWavFile(opusFile):
  
    wavFileName = opusFile[25:].replace("opus","wav")
    
    query = "ffmpeg -i " + opusFile + " " + wavFileName
    response = subprocess.Popen(query, shell=True, stdout=subprocess.PIPE).stdout.read()
    s = str(response).encode('utf-8')
    wavFilePath = os.path.join(os.getcwd(), wavFileName)

    return wavFilePath, wavFileName