import maestro
import time
import logging

logging.basicConfig(level=logging.INFO)

commandDelay = 0.1 #seconds between commands; we need a short time for the message to get to the controller

cigChannel = 1
cigAccel = 10
cigDim = 5
cigBright = 24000

armChannel = 0
armAccel = 5
armDown = 9000
armUp = 3000

speed = None

servo =  maestro.Controller() #/dev/ttyACM1 or ttyACM0(default)

try:
    
    logging.info(f'starting armChannel: {armChannel} cigChannel: {cigChannel} armAccel:{armAccel} cigAccel:{cigAccel}')

    #init
    servo.setAccel(cigChannel, cigAccel)
    time.sleep(commandDelay)
    servo.setTarget(cigChannel,cigDim)
    time.sleep(commandDelay)
    
    servo.setAccel(armChannel, armAccel)
    time.sleep(commandDelay)
    servo.setTarget(armChannel,armDown)
    time.sleep(commandDelay)
    
    #servo.setSpeed(channelIndex, speed)   

    while True: 
        time.sleep(5)

        #move arm
        servo.setTarget(armChannel,armUp)
        time.sleep(2)

        #cig time
        servo.setTarget(cigChannel,cigBright)
        time.sleep(2)

        servo.setTarget(cigChannel,cigDim)
        time.sleep(commandDelay)

        #move arm back    
        servo.setTarget(armChannel,armDown)

finally:
    logging.info('closing connection')
    servo.close()
