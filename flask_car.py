'''
Author: TEO Cheng Guan

Simple remote control car. (RPI)

This app runs on RPI4 with 2 servo motors connected to ch0 and ch1 of the RPI4 servo hat.
It hosts a micro service to receive command on port 5000.

'''

from flask import Flask, request, render_template
import datetime

import servo
from PCA9685 import *

pwm = PCA9685(0x40, debug=False)
pwm.setPWMFreq(50)

ch0 = servo.servo(pwm, 0)
ch1 = servo.servo(pwm, 1)

app = Flask(__name__)

@app.route("/move", methods=['GET'])
def move():
    if request.method == 'GET':
        # Get the foreground and background color from input argument. Apply back and white if not found.
        direction = request.args.get('direction')

        if (direction == 'up'):
            print('Up pressed')
            ch0.move(200)
            ch1.move(700)
        elif (direction == 'stop'):
            print('Up/down released')
            ch0.stop()
            ch1.stop()
        elif (direction == 'down'):
            print('Down pressed')
            ch0.move(700)
            ch1.move(200)
        elif (direction == 'left'):
            print('Left pressed')
            ch0.move(200)
            ch1.move(345)
        elif (direction == 'right'):
            print('Right pressed')
            ch0.move(330)
            ch1.move(700)

        return direction

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)