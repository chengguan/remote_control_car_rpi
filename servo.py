import time

class servo:

    def __init__(self, servo_drv, channel=0):
        self.channel = channel
        self.speed = 0
        self.run_worker = True
        self.servo_drv = servo_drv

    def move(self, speed):
        self.servo_drv.setPWM(self.channel, 0, speed)

    def stop(self):
        self.servo_drv.setPWM(self.channel, 0, 0)

 