import wiringpi
from time import sleep

SLEEP_TIME = 0.5


def init():
    wiringpi.wiringPiSetup()
    wiringpi.pinMode(21, 1)
    wiringpi.pinMode(22, 1)
    wiringpi.pinMode(23, 1)
    wiringpi.pinMode(24, 1)
    wiringpi.pinMode(25, 1)
    wiringpi.pinMode(27, 1)
    wiringpi.pinMode(28, 1)
    wiringpi.pinMode(29, 1)


def forward():
    print("Moving forward")
    wiringpi.digitalWrite(21, 1)
    wiringpi.digitalWrite(22, 1)
    wiringpi.digitalWrite(25, 1)
    wiringpi.digitalWrite(27, 1)
    sleep(SLEEP_TIME)
    wiringpi.digitalWrite(21, 0)
    wiringpi.digitalWrite(22, 0)
    wiringpi.digitalWrite(25, 0)
    wiringpi.digitalWrite(27, 0)


def back():
    print("Moving backward")
    wiringpi.digitalWrite(23, 1)
    wiringpi.digitalWrite(24, 1)
    wiringpi.digitalWrite(28, 1)
    wiringpi.digitalWrite(29, 1)
    sleep(SLEEP_TIME)
    wiringpi.digitalWrite(23, 0)
    wiringpi.digitalWrite(24, 0)
    wiringpi.digitalWrite(28, 0)
    wiringpi.digitalWrite(29, 0)

def left():
    print("Moving left")
    wiringpi.digitalWrite(22, 1)
    sleep(SLEEP_TIME)
    wiringpi.digitalWrite(22, 0)


def right():
    print("Moving right")
    wiringpi.digitalWrite(21, 1)
    sleep(SLEEP_TIME)
    wiringpi.digitalWrite(21, 0)


def stop():
    print("Stop!")
    wiringpi.digitalWrite(21, 0)
    wiringpi.digitalWrite(22, 0)
    wiringpi.digitalWrite(23, 0)
    wiringpi.digitalWrite(24, 0)
    wiringpi.digitalWrite(25, 0)
    wiringpi.digitalWrite(27, 0)
    wiringpi.digitalWrite(28, 0)
    wiringpi.digitalWrite(29, 0)