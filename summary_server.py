from __future__ import unicode_literals
from flask import Flask, render_template, url_for, request, jsonify, make_response, Response, send_file, session
from utils.getMeetingInfo import getcurrentMeetingInfo
import os

app = Flask(__name__)

CONF_ID = ""
MEETING_START_TIME = ""
PARTICIPANT_LIST = ""
FINAL_SUMMARY = ""
SUM_LEN = ""
app.secret_key = 'nevertellthistoanyone'
SUMMARY = "52699_summary.txt"


def loadMeetingInformation():
    pStr = ""
    #Step 1: Get the Current Meeting Information
    currentMeetingInfo = getcurrentMeetingInfo()

    CONF_ID = currentMeetingInfo['voiceConfID']
    session['CONF_ID'] = currentMeetingInfo['voiceConfID']
    MEETING_START_TIME = currentMeetingInfo['recordTimeStamp']
    session['MEETING_START_TIME'] = currentMeetingInfo['recordTimeStamp']

    participantList = currentMeetingInfo['userNames']
    for p in participantList:
        pStr = pStr + str(p) + ", "
    
    PARTICIPANT_LIST = pStr
    session['PARTICIPANT_LIST'] = PARTICIPANT_LIST
    #summaryFileName = os.getcwd() + "/MeetingSummaryData/" + CONF_ID + "_summary.txt"
    summaryFileName = os.getcwd() + "/MeetingSummaryData/" + SUMMARY

    fSummary = open(summaryFileName, "r")
    final_summary = fSummary.read()
    FINAL_SUMMARY = final_summary

    session['SUM_LEN'] = 100
    SUM_LEN = str(session.get('SUM_LEN'))

    return CONF_ID, MEETING_START_TIME, PARTICIPANT_LIST, FINAL_SUMMARY, SUM_LEN
    


@app.route('/', methods=['GET','POST'])
def index():
    CONF_ID, MEETING_START_TIME, PARTICIPANT_LIST, FINAL_SUMMARY, SUM_LEN = loadMeetingInformation()
    return render_template('index.html',conf_id=CONF_ID,meeting_start_time=MEETING_START_TIME,participant_list=PARTICIPANT_LIST, sum_len=SUM_LEN, final_summary=FINAL_SUMMARY)


@app.route("/newroute")
def newroute():

    CONF_ID = str(session.get('CONF_ID'))
    summaryFileName = os.getcwd() + "/MeetingSummaryData/" + str(CONF_ID) + "_summary.txt"

    #Step 2: Get the meeting summary so far
    fSummary = open(summaryFileName, "r")
    final_summary = fSummary.read()
    FINAL_SUMMARY = final_summary

    MEETING_START_TIME = str(session.get('MEETING_START_TIME'))
    PARTICIPANT_LIST = str(session.get('PARTICIPANT_LIST'))
    SUM_LEN = str(session.get('SUM_LEN'))

    return render_template('index.html',conf_id=CONF_ID,meeting_start_time=MEETING_START_TIME,participant_list=PARTICIPANT_LIST, sum_len=SUM_LEN, final_summary=FINAL_SUMMARY)


@app.route("/getPDF")
def getPDF():
    conf_id = session.get('CONF_ID')
    summaryFileName = os.getcwd() + "/MeetingSummaryData/PDF/" + str(conf_id) + "_summary.pdf"
    fName = str(conf_id) + "_summary.pdf"
    try:
        return send_file(summaryFileName, attachment_filename=fName)
    except Exception as e:
        return str(e)
  
if __name__ == '__main__':
    app.run(host='localhost', port=7030, debug=True)
