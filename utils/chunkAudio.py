#Convert Opus to Wav
#Split them to less than a minute and store it in /tmp

import os
import subprocess

# Only for test
# opusFile = "data/cde145e5c20766d33c81bb492a157a94feb3a0f1-1603617884026-15243890485.opus"

def createConfTemp(CONF_ID):
    path = os.path.join(os.getcwd(), "audio/tmp", str(CONF_ID))
    isdir = os.path.isdir(path)
    if not isdir:
        os.mkdir(path)
        status = "Path: " + path + " created successfully!"
    else:
        status = "Path: " + path + " already exists!"
    return status, path

def chuckAudio(wavFilePath, CONF_ID):

    #create tmp folder for conf ID
    status, path = createConfTemp(CONF_ID)
    print(status)

    query = "ffmpeg -i " + wavFilePath +  " -f segment -segment_time 59 -c copy " + path + "/output%09d.wav"
    response = subprocess.Popen(query, shell=True, stdout=subprocess.PIPE).stdout.read()
    s = str(response).encode('utf-8')
    print("Sub audios created successfully" + str(s))

    return path


