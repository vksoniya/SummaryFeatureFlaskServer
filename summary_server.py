from __future__ import unicode_literals
from flask import Flask, render_template, url_for, request
import time
from utils.getMeetingInfo import getcurrentMeetingInfo

app = Flask(__name__)

CONF_ID = ""
MEETING_START_TIME = ""
PARTICIPANT_LIST = ""
FINAL_SUMMARY = ""

@app.route('/')
def index():
        pStr = ""
        #Step 1: Get the Current Meeting Information
        currentMeetingInfo = getcurrentMeetingInfo()
        CONF_ID = currentMeetingInfo['voiceConfID']
        MEETING_START_TIME = currentMeetingInfo['recordTimeStamp']
        participantList = currentMeetingInfo['userNames']
        for p in participantList:
            pStr = pStr + str(p) + ", "
        PARTICIPANT_LIST = pStr
        #Step 2: Load <confid>_summary.txt content
        #currentSummaryFile = "MeetingSummaryData/" + conf_id + "_summary.txt" # Actual file
        currentSummaryFile = "MeetingSummaryData/88503_summary.txt" #This filename will
        fSummary = open(currentSummaryFile, "r")
        final_summary = fSummary.read()
        FINAL_SUMMARY = final_summary
        return render_template('index.html',conf_id=CONF_ID,meeting_start_time=MEETING_START_TIME,participant_list=PARTICIPANT_LIST,final_summary=FINAL_SUMMARY)

#Pending Reload summary on button click
# Alternate use stream, as last option
@app.route('/',methods=['GET','POST'])
def refresh():
    final_summary = ""
    if request.method == 'POST':
        final_summary = "underconstruction"
        FINAL_SUMMARY = final_summary
    return render_template('index.html',conf_id=CONF_ID,meeting_start_time=MEETING_START_TIME,participant_list=PARTICIPANT_LIST,final_summary=FINAL_SUMMARY)

if __name__ == '__main__':
    app.run(host='localhost', port=7030, debug=True)
