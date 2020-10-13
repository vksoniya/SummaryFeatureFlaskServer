from __future__ import unicode_literals
from flask import Flask, render_template, url_for, request
import time
from utils.getMeetingInfo import getcurrentMeetingInfo

app = Flask(__name__)

@app.route('/')
def index():
        pStr = ""
        #Step 1: Get the Current Meeting Information
        currentMeetingInfo = getcurrentMeetingInfo()
        conf_id = currentMeetingInfo['voiceConfID']
        meeting_start_time = currentMeetingInfo['recordTimeStamp']
        participantList = currentMeetingInfo['userNames']
        for p in participantList:
            pStr = pStr + str(p) + ", "
        participant_list = pStr
        #Step 2: Load <confid>_summary.txt content
        #currentSummaryFile = "MeetingSummaryData/" + conf_id + "_summary.txt" # Actual file
        currentSummaryFile = "MeetingSummaryData/88503_summary.txt" #This filename will
        fSummary = open(currentSummaryFile, "r")
        final_summary = fSummary.read()
        return render_template('index.html',conf_id=conf_id,meeting_start_time=meeting_start_time,participant_list=participant_list,final_summary=final_summary)

if __name__ == '__main__':
    app.run(host='localhost', port=7030, debug=True)
