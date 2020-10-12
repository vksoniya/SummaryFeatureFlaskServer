from __future__ import unicode_literals
from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
        return render_template('index.html')

if __name__ == '__main__':
    app.run(host='localhost', port=7030, debug=True)
