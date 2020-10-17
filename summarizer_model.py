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

def extractConfID():
    currentMeetingInfo = getcurrentMeetingInfo()
    CONF_ID = currentMeetingInfo['voiceConfID']
    return CONF_ID

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
        print(sText[0]['summary_text'])

        tFile = open(summaryFile, "a")
        m = str(sText[0]['summary_text'])
        tFile = open(summaryFile, "a")
        tFile.write(m)
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
    CONF_ID = extractConfID()
    print("ConfID:" + CONF_ID)
    summaryFile = createSummaryFile()
    print("Created Summary File:" + summaryFile)
    transcriptFile = getTranscriptFile()
    print("Got Transcript File Name:" + transcriptFile)
    #Step2
    #create summary and write to file above
    #status = generateSummary(summaryFile, transcriptFile)
    #print(status)


   