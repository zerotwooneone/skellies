import maestro
import time
import logging

logging.basicConfig(level=logging.INFO)

commandDelay = 2 #seconds between commands
channelIndex = 2    
accel = 5
#speed = 

servo =  maestro.Controller() #/dev/ttyACM1 or ttyACM0(default)

try:
    
    logging.info(f'starting channelIndex: {channelIndex} accel:{accel} speed:{speed or "not set"}')
    
    servo.setAccel(channelIndex, accel)    
    
    #servo.setSpeed(channelIndex, speed)    
    
    servo.setTarget(channelIndex,3000)
    servo.setTarget(channelIndex,9000)
finally:
    logging.info('closing connection')
    servo.close()