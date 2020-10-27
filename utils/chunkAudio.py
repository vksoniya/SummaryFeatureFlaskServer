#Convert Opus to Wav
#Split them to less than a minute and store it in /tmp

import os
import subprocess
from utils.convertToWav import convertToWavFile

# Only for test
# opusFile = "data/cde145e5c20766d33c81bb492a157a94feb3a0f1-1603617884026-15243890485.opus"

def chuckAudio(opusFile):
    wavFilePath, wavFileName = convertToWavFile(opusFile)
    print(wavFilePath)
    print(wavFileName)

    #wavFileName = "bb492a157a94feb3a0f1-1603617884026-15243890485.wav"

    query = "ffmpeg -i " + wavFileName +  " -f segment -segment_time 50 -c copy tmp/output%09d.wav"
    response = subprocess.Popen(query, shell=True, stdout=subprocess.PIPE).stdout.read()
    s = str(response).encode('utf-8')
    print("Sub audios created successfully" + str(s))

    return wavFilePath


