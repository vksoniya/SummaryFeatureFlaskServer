from __future__ import unicode_literals
from flask import Flask, render_template, url_for, request, jsonify, make_response, Response, send_file
from utils.getMeetingInfo import getcurrentMeetingInfo
import os

app = Flask(__name__)

CONF_ID = ""
MEETING_START_TIME = ""
PARTICIPANT_LIST = ""
FINAL_SUMMARY = ""
SUM_LEN = ""

def loadMeetingInformation():
    pStr = ""
    #Step 1: Get the Current Meeting Information
    currentMeetingInfo = getcurrentMeetingInfo()

    CONF_ID = currentMeetingInfo['voiceConfID']
    session['CONF_ID'] = currentMeetingInfo['voiceConfID']
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
    CONF_ID, MEETING_START_TIME, PARTICIPANT_LIST, FINAL_SUMMARY = loadMeetingInformation()
    SUM_LEN = 100
    return render_template('index.html',conf_id=CONF_ID,meeting_start_time=MEETING_START_TIME,participant_list=PARTICIPANT_LIST, sum_len=SUM_LEN, final_summary=FINAL_SUMMARY)



@app.route("/getPDF")
def getPDF():
    # with open("outputs/Adjacency.csv") as fp:
    #     csv = fp.read()
    conf_id = session.get('CONF_ID')
    summaryFileName = os.getcwd() + "/MeetingSummaryData/PDF/" + conf_id + "_summary.pdf"
    fName = conf_id + "_summary.pdf"
    try:
        #return send_file('/var/www/PythonProgramming/PythonProgramming/static/ohhey.pdf', attachment_filename='ohhey.pdf')
        return send_file(summaryFileName, attachment_filename=fName)
    except Exception as e:
        return str(e)
    #csv = '1,2,3\n4,5,6\n'
    #return Response(csv, mimetype="text/csv", headers={"Content-disposition": "attachment; filename=myplot.csv"})

if __name__ == '__main__':
    app.run(host='localhost', port=7030, debug=True)
