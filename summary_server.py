from __future__ import unicode_literals
from flask import Flask, render_template, url_for, request, jsonify, make_response, Response
from utils.getMeetingInfo import getcurrentMeetingInfo
import os

app = Flask(__name__)

CONF_ID = ""
MEETING_START_TIME = ""
PARTICIPANT_LIST = ""
FINAL_SUMMARY = ""

def loadMeetingInformation(location):
    pStr = ""
    #Step 1: Get the Current Meeting Information
    currentMeetingInfo = getcurrentMeetingInfo()

    CONF_ID = currentMeetingInfo['voiceConfID']
    MEETING_START_TIME = currentMeetingInfo['recordTimeStamp']

    participantList = currentMeetingInfo['userNames']
    for p in participantList:
        pStr = pStr + str(p) + ", "
    
    PARTICIPANT_LIST = pStr
    summaryFileName = os.getcwd() + "/MeetingSummaryData/" + CONF_ID + "_summary.txt"

    #Step 2: Get the meeting summary so far
    fSummary = open(summaryFileName, "r")
    final_summary = fSummary.read()
    FINAL_SUMMARY = final_summary
    return CONF_ID, MEETING_START_TIME, PARTICIPANT_LIST, FINAL_SUMMARY
    


@app.route('/', methods=['GET','POST'])
def index():
    CONF_ID, MEETING_START_TIME, PARTICIPANT_LIST, FINAL_SUMMARY = loadMeetingInformation("1")
    
    return render_template('index.html',conf_id=CONF_ID,meeting_start_time=MEETING_START_TIME,participant_list=PARTICIPANT_LIST,final_summary=FINAL_SUMMARY)


if __name__ == '__main__':
    app.run(host='localhost', port=7030, debug=True)
