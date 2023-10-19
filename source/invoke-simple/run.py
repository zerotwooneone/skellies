import maestro
import time
import logging

logging.basicConfig(level=logging.INFO)

commandDelay = 2 #seconds between commands
cigChannel = 1
armChannel = 0
armAccel = 5
cigAccel = 1
speed = None

servo =  maestro.Controller() #/dev/ttyACM1 or ttyACM0(default)

try:
    
    logging.info(f'starting channelIndex: {channelIndex} accel:{armAccel} speed:{speed}')
    
    #setup arm
    servo.setAccel(armChannel, armAccel)
    time.sleep(1)    
    #servo.setSpeed(channelIndex, speed)    
    
    #move arm
    servo.setTarget(armChannel,3000)
    time.sleep(commandDelay)

    #cig time
    servo.setAccel(cigChannel, cigAccel)
    time.sleep(1)

    servo.setTarget(cigChannel,12000)
    time.sleep(commandDelay)

    servo.setTarget(cigChannel,0)
    time.sleep(commandDelay)

    #move arm back    
    servo.setTarget(armChannel,9000)
    
finally:
    logging.info('closing connection')
    servo.close()
