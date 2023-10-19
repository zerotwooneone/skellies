import maestro
import time
import logging

logging.basicConfig(level=logging.INFO)

commandDelay = 2 #seconds between commands
channelIndex = 2    
accel = 5

servo =  maestro.Controller() #/dev/ttyACM1 or ttyACM0(default)

try:
    
    servo.setAccel(channelIndex, accel)
    
    #speed = 
    #servo.setSpeed(channelIndex, speed)
    
    logging.debug(f'about to goTo channelIndex: {channelIndex} accel:{accel} speed:{speed} target:{target}')
    servo.setTarget(channelIndex,3000)
    servo.setTarget(channelIndex,9000)
finally:
    logging.info('closing connection')
    servo.close()