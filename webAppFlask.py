# pip install flask if not installed
# don't name your file as flask.py !
from flask import Flask, redirect, url_for, request, render_template
from bs4 import BeautifulSoup as bs
import requests
import json

import ev3dev.ev3 as ev3

# create a Flask object
app = Flask(__name__)


# load the question webpage
@app.route('/')
def load_webpage():
    return json.dumps({"load": "Success"})

@app.route('/init',methods=['GET'])
def robotArm():
    if request.values.get("variable").lower() == "extend".lower():
        try:
            # edit here
            m = ev3.LargeMotor('outA')
            m.run_timed(time_sp=3000, speed_sp=500)
            # end edit
            return json.dumps({"receivedRequest": "true", "variable": "extend","error":"None"})
        except:
            return json.dumps({"receivedRequest": "false", "variable": "None","error":"Error when controlling arm"})

    elif request.values.get("variable").lower() == "retract".lower():
        try:

            #edit here
            m = ev3.LargeMotor('outA')
            m.run_timed(time_sp=3000, speed_sp=500)

            #end edit
            return json.dumps({"receivedRequest": "true", "variable": "retract","error":"None"})
        except:
            return json.dumps({"receivedRequest": "false", "variable": "None","error":"Error when controlling arm"})


    else:
        return json.dumps({"receivedRequest": "false", "variable": "None","error":"Get param error"})



# run the app
if __name__ == '__main__':
    app.run(debug = True,host='0.0.0.0', port=8080)

