# Michael Hartle & Xiaojing Xia
# Session:B03
# GTID: 902973320 / 902999067
# mhartle@gatech.edu / xxia34@gatech.edu
# We worked on this assignment alone, using only this semester's course materials.

from Myro import *
init("/dev/tty.scribbler")

def avoidWalls():
    for t in timer(60):
        forward(.4)
        while getObstacle("center") > 5400 or getObstacle("right") > 5750:
            turnLeft(.4)
    turnLeft(1)
    beep(.25,784)
    beep(.25,784)
    beep(.25,1174.7)
    beep(.25,1174.7)
    beep(.25,1318.5)
    beep(.25,1318.5)
    beep(.5,1174.7)

    beep(.25,1046.5)
    beep(.25,1046.5)
    beep(.25,987.8)
    beep(.25,987.8)
    beep(.25,880)
    beep(.25,880)
    beep(1,784)
    stop()
    for i in range(3):
        turnLeft(1,.4)
        turnRight(1,.4)

