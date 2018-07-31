#!/usr/bin/env python

import rospy
from flask import Flask
from flask import request

app = Flask(__name__, static_folder='../src/static/')

@app.route('/')
def home():
    return app.send_static_file('index.html')

if __name__ == "__main__":
    rospy.init_node('web_console')
    app.run(host='0.0.0.0', port=9999, threaded=True)
