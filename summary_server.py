from __future__ import unicode_literals
from flask import Flask, render_template, url_for, request, jsonify, make_response
import time
from utils.getMeetingInfo import getcurrentMeetingInfo

app = Flask(__name__)

CONF_ID = ""
MEETING_START_TIME = ""
PARTICIPANT_LIST = ""
FINAL_SUMMARY = ""

def loadMeetingInformation(location):
    if (location == '1'):
        pStr = ""
        #Step 1: Get the Current Meeting Information
        currentMeetingInfo = getcurrentMeetingInfo()
        CONF_ID = currentMeetingInfo['voiceConfID']
        MEETING_START_TIME = currentMeetingInfo['recordTimeStamp']
        participantList = currentMeetingInfo['userNames']
        for p in participantList:
            pStr = pStr + str(p) + ", "
        PARTICIPANT_LIST = pStr
        currentSummaryFile = "MeetingSummaryData/88503_summary.txt" #This filename will
        fSummary = open(currentSummaryFile, "r")
        final_summary = fSummary.read()
        FINAL_SUMMARY = final_summary
        #CONF_ID = currentMeetingInfo['voiceConfID']
        return CONF_ID, MEETING_START_TIME, PARTICIPANT_LIST, FINAL_SUMMARY
    if (location == '2'):
        currentSummaryFile = "MeetingSummaryData/88503_summary.txt" #This filename will
        fSummary = open(currentSummaryFile, "r")
        final_summary = fSummary.read()
        FINAL_SUMMARY = final_summary
        return CONF_ID, MEETING_START_TIME, PARTICIPANT_LIST, FINAL_SUMMARY


@app.route('/', methods=['GET','POST'])
def index():
    CONF_ID, MEETING_START_TIME, PARTICIPANT_LIST, FINAL_SUMMARY = loadMeetingInformation("1")
    return render_template('index.html',conf_id=CONF_ID,meeting_start_time=MEETING_START_TIME,participant_list=PARTICIPANT_LIST,final_summary=FINAL_SUMMARY)


@app.route('/stream')
def stream():
    def eventStream():
        while True:
            # wait for source data to be available, then push it
            sum_text = loadMeetingInformation()
            CONF_ID, MEETING_START_TIME, PARTICIPANT_LIST, FINAL_SUMMARY = loadMeetingInformation("2")
            yield 'data: {}\n\n'.format(FINAL_SUMMARY)
    return Response(eventStream(), mimetype="text/event-stream")


if __name__ == '__main__':
    app.run(host='localhost', port=7030, debug=True)
