import pandas as pd
import os
from transformers import pipeline
import textwrap

#transcriptFile = "29499_transcript.txt"
#summaryFile = "29499_summary1.txt"
rText =  ""
CONF_ID = "29499"

def generateSummary(summaryFile, transcriptFile):
    summarizer = pipeline("summarization") #Default BART model 
    n = 2500 # Summarizer length parameter dependent on the summarization method


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

    return status

def createSummaryFile(CONF_ID):
    fName = "~/MeetingSummaryData/" + CONF_ID + "_summary.txt"
    return fName

def getTranscriptFile(CONF_ID):
    fName = "~/MeetingTranscriptData/" + CONF_ID + "_transcript.txt"
    return fName

if __name__ == '__main__':
    #Step 1:
    #Create summary file <confid>_summary.txt
    #Storage path: "/MeetingSummaryData"
    summaryFile = createSummaryFile(CONF_ID)
    transcriptFile = getTranscriptFile(CONF_ID)
    #Step2
    #create summary and write to file above
    status = generateSummary(summaryFile, transcriptFile)
    print(status)


   