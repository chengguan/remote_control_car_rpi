import datetime
import time
import importlib

import smbus
#from inputs import get_gamepad
import inputs
import servo
from PCA9685 import *


def main():
    pwm = PCA9685(0x40, debug=False)
    pwm.setPWMFreq(50)

    ch0 = servo.servo(pwm, 0)
    ch1 = servo.servo(pwm, 1)

    while 1:
        try:
            events = inputs.get_gamepad()
        except inputs.UnpluggedError:
            print(f'Gamepad lost. Retrying...')
            events = []
            time.sleep(1)
            importlib.reload(inputs)
            continue
            
        except OSError as err:
            print(f'Gamepad lost. Retrying...OSError')
            events = []
            time.sleep(1)
            importlib.reload(inputs)
            continue

        except KeyboardInterrupt:
            print("Exiting...")
            break

        for event in events:
            #timestamp = 'Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
            #print(f"{timestamp}: {event.ev_type}-{event.code}-{event.state}")

            if (event.ev_type=='Absolute') & (event.code=='ABS_Y') & (event.state==0):
                print('Up pressed')
                ch0.forward()
                ch1.reverse()
            elif (event.ev_type=='Absolute') & (event.code=='ABS_Y') & (event.state==127):
                print('Up/down released')
                ch0.stop()
                ch1.stop()
            elif (event.ev_type=='Absolute') & (event.code=='ABS_Y') & (event.state==255):
                print('Down pressed')
                ch0.reverse()
                ch1.forward()
            elif (event.ev_type=='Absolute') & (event.code=='ABS_X') & (event.state==0):
                print('Left pressed')
                ch0.forward()
                ch1.forward()
            elif (event.ev_type=='Absolute') & (event.code=='ABS_X') & (event.state==127):
                print('Left/right release')
                ch0.stop()
                ch1.stop()
            elif (event.ev_type=='Absolute') & (event.code=='ABS_X') & (event.state==255):
                print('Right pressed')
                ch0.reverse()
                ch1.reverse()
    
    ch0.stop()
    ch1.stop()

if __name__ == "__main__":
    main()
