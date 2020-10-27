import pandas as pd
import os
from transformers import pipeline
import textwrap
from utils.getMeetingInfo import getcurrentMeetingInfo
from utils.watchDog import watch_dog

#This server will create summary and write a summary file
# <confid>_summary.txt to the /MeetingSummaryData location

#transcriptFile = "29499_transcript.txt"
#summaryFile = "29499_summary1.txt"
CONF_ID = ""

def extractConfInfo():
    currentMeetingInfo = getcurrentMeetingInfo()
    CONF_ID = currentMeetingInfo['voiceConfID']
    RECORD_PATH = currentMeetingInfo['RecordPath']
    return CONF_ID, RECORD_PATH


def createSummaryFile():
    fName = os.getcwd() + "/MeetingSummaryData/" + CONF_ID + "_summary.txt"
    return fName

def getTranscriptFile():
    fName = os.getcwd() + "/MeetingTranscriptData/" + CONF_ID + "_transcript.txt"
    return fName

def initSummarizer():
    summarizer = pipeline("summarization") #Default BART model 
    n = 2500 # Summarizer length parameter dependent on the summarization method
    return summarizer

def generateSummary(summaryFile, transcriptFile):
    summarizer = initSummarizer()
   
    if watch_dog(transcriptFile):
        #Create Summary
        print("=" * 100)
        print("2.Summarizing " + str(transcriptFile))
        print("=" * 100)
        df = pd.read_csv(transcriptFile, sep='delimiter', header=None, names=["Transcript"])
            
        ARTICLE = str(df['Transcript'])
        sText = summarizer(ARTICLE, max_length=100, min_length=30, do_sample=False)
        t = sText[0]['summary_text']
        #print(sText[0]['summary_text'])
        temp = t[38:]
        print(t[38:]) #quick hack to fix text details

        tFile = open(summaryFile, "a")
        m = str(sText[0]['summary_text']) #to be corrected later
        tFile = open(summaryFile, "a")
        tFile.write(temp)
        tFile.flush()
        tFile.close()

        status = "Sucessfully summarized"

    else:
        status = "Nothing to summarize"

    return status


if __name__ == '__main__':
    #Step 1:
    #Create summary file <confid>_summary.txt
    #Storage path: "/MeetingSummaryData"
    CONF_ID, RECORD_PATH = extractConfInfo()
    print("ConfID:" + CONF_ID)
    print("Record Path:" + RECORD_PATH)
    summaryFile = createSummaryFile()
    print("Created Summary File:" + summaryFile)
    transcriptFile = getTranscriptFile()
    print("Got Transcript File Name:" + transcriptFile)
    #Step2
    #create summary and write to file above
    status = generateSummary(summaryFile, transcriptFile)
    print(status)


   