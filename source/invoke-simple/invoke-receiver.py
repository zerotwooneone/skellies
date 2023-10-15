from dapr.ext.grpc import App, InvokeMethodRequest, InvokeMethodResponse
import maestro
import time
import logging
import json

logging.basicConfig(level=logging.INFO)
app = App()

@app.method(name='my-method')
def mymethod(request: InvokeMethodRequest) -> InvokeMethodResponse:
    logging.info(request.metadata)
    logging.info(request.text())    

    return InvokeMethodResponse(b'INVOKE_RECEIVED', "text/plain; charset=UTF-8")

@app.method(name='testRange')
def testRange(request: InvokeMethodRequest) -> InvokeMethodResponse:
    logging.info(request.metadata)
    logging.info(request.text())

    logging.info('received testRange')
    servo =  maestro.Controller() #/dev/ttyACM1 or ttyACM0(default)

    channels = [0] #range(18)
    targets = [3000, 3500, 6500, 8000,9000] #[1,2000,3000,4000,6000,8000,9000]
    #speeds = [0,1,60]
    accels = [1] #,100,255
    try:
        #for speed in speeds:
        for acc in accels:
            for target in targets:
                for channelIndex in channels:
                    logging.info(f'ch: {channelIndex} acc:{acc} tar:{target}')
                    logging.info(f'min:{servo.getMin(channelIndex)} max:{servo.getMax(channelIndex)} pos:{servo.getPosition(channelIndex)} isMov:{servo.isMoving(channelIndex)} gMov:{servo.getMovingState()}')
                    #servo.setSpeed(channelIndex,speed)
                    servo.setAccel(channelIndex,acc)
                    servo.setTarget(channelIndex,target)
                    time.sleep(5)
    finally:
        logging.info('closing connection')
        servo.close()

    return InvokeMethodResponse(b'INVOKE_RECEIVED', "text/plain; charset=UTF-8")

@app.method(name='goTo')
def goTo(request: InvokeMethodRequest) -> InvokeMethodResponse:
    logging.info('received goTo')
    #print(request.metadata, flush=True)
    logging.info("request text" + request.text())

    dict = json.loads(request.text())
    if("channelIndex" not in dict):
        logging.error("missing channel index")
        return InvokeMethodResponse(b'INVOKE_RECEIVED', "text/plain; charset=UTF-8")
    
    servo =  maestro.Controller() #/dev/ttyACM1 or ttyACM0(default)

    try:
        channelIndex = dict["channelIndex"]
        target = dict["target"]
        if("speed" in dict):
            speed = dict["speed"]
            servo.setSpeed(channelIndex, speed)
        if("accel" in dict):
            accel = dict["accel"]
            servo.setAccel(channelIndex, accel)
        logging.debug(f'about to goTo channelIndex: {channelIndex} accel:{accel} speed:{speed} target:{target}')
        servo.setTarget(channelIndex,target)
    finally:
        logging.info('closing connection')
        servo.close()

    return InvokeMethodResponse(b'INVOKE_RECEIVED', "text/plain; charset=UTF-8")

@app.method(name='setAcceleration')
def setAcceleration(request: InvokeMethodRequest) -> InvokeMethodResponse:
    logging.debug(request.metadata)
    logging.debug("request text" + request.text())

    dict = json.loads(request.text())
    if("channelIndex" not in dict):
        logging.error("missing channel index")
        return InvokeMethodResponse(b'INVOKE_RECEIVED', "text/plain; charset=UTF-8")
    if("accel" not in dict):
        logging.error("missing acceleration [accel]")
        return InvokeMethodResponse(b'INVOKE_RECEIVED', "text/plain; charset=UTF-8")

    servo =  maestro.Controller() #/dev/ttyACM1 or ttyACM0(default)

    try:        
        channelIndex = dict["channelIndex"]
        accel = dict["accel"]
        logging.debug(f'about to set acceleration: {channelIndex} accel:{accel}')
        servo.setAccel(channelIndex, accel)        
    finally:
        logging.debug('closing connection')
        servo.close()

    return InvokeMethodResponse(b'INVOKE_RECEIVED', "text/plain; charset=UTF-8")

@app.method(name='setSpeed')
def setSpeed(request: InvokeMethodRequest) -> InvokeMethodResponse:
    logging.debug(request.metadata)
    logging.debug("request text" + request.text())

    dict = json.loads(request.text())
    if("channelIndex" not in dict):
        logging.error("missing channel index")
        return InvokeMethodResponse(b'INVOKE_RECEIVED', "text/plain; charset=UTF-8")
    if("speed" not in dict):
        logging.error("missing speed [speed]")
        return InvokeMethodResponse(b'INVOKE_RECEIVED', "text/plain; charset=UTF-8")

    servo =  maestro.Controller() #/dev/ttyACM1 or ttyACM0(default)

    try:        
        channelIndex = dict["channelIndex"]
        speed = dict["speed"]
        logging.debug(f'about to set speed: {channelIndex} speed:{speed}')
        servo.setSpeed(channelIndex, speed)        
    finally:
        logging.debug('closing connection')
        servo.close()

    return InvokeMethodResponse(b'INVOKE_RECEIVED', "text/plain; charset=UTF-8")

app.run(50051)