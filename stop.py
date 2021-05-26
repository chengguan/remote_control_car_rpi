#from __future__ import print_function

import datetime
import time
import math
import threading

import smbus
from inputs import get_gamepad
import servo
from PCA9685 import *

def main():
    pwm = PCA9685(0x40, debug=False)
    pwm.setPWMFreq(50)

    ch0 = servo.servo(pwm, 0)
    ch1 = servo.servo(pwm, 1)

    ch0.stop()
    ch1.stop()

if __name__ == "__main__":
    main()