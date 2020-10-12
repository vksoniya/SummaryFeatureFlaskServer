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
            name = str(p) + ", "
            pStr = pStr + name
        participant_1 = pStr
        participant_2 = "Vindhya"
        final_summary = "Some random stuff that we talk about"
        return render_template('index.html',conf_id=conf_id,meeting_start_time=meeting_start_time,participant_1=participant_1,participant_2=participant_2,final_summary=final_summary)

if __name__ == '__main__':
    app.run(host='localhost', port=7030, debug=True)
