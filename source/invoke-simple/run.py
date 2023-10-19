import maestro
import time
import logging

logging.basicConfig(level=logging.INFO)

commandDelay = 0.1 #seconds between commands
cigChannel = 1
armChannel = 0
armAccel = 5
cigAccel = 10
speed = None

servo =  maestro.Controller() #/dev/ttyACM1 or ttyACM0(default)

try:
    
    logging.info(f'starting armChannel: {armChannel} cigChannel: {cigChannel} armAccel:{armAccel} cigAccel:{cigAccel}')
    
    #setup arm
    servo.setAccel(armChannel, armAccel)
    time.sleep(1)    
    #servo.setSpeed(channelIndex, speed)    
    
    #move arm
    servo.setTarget(armChannel,3000)
    #time.sleep(commandDelay)

    #cig time
    servo.setAccel(cigChannel, cigAccel)
    time.sleep(commandDelay)

    servo.setTarget(cigChannel,12000)
    time.sleep(2)

    servo.setTarget(cigChannel,10)
    time.sleep(3)

    #move arm back    
    servo.setTarget(armChannel,9000)

finally:
    logging.info('closing connection')
    servo.close()
