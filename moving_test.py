import moving
from time import sleep

moving.SLEEP_TIME = 1
moving.init()

while True:
    moving.forward()
    moving.left()
    moving.right()
    moving.back()
    moving.stop()
    sleep(1)