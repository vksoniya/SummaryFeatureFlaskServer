from __future__ import unicode_literals
from flask import Flask, render_template, url_for, request
import time

app = Flask(__name__)

@app.route('/')
def index():
        conf_id = "12345"
        meeting_start_time = time.time()
        participant_1 = "Soniya"
        participant_2 = "Vindhya"
        final_summary = "Some random stuff that we talk about"
        return render_template('index.html',conf_id=conf_id,meeting_start_time=meeting_start_time,participant_1=participant_1,participant_2=participant_2,final_summary=final_summary)

if __name__ == '__main__':
    app.run(host='localhost', port=7030, debug=True)
