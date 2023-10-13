from dapr.ext.grpc import App, InvokeMethodRequest, InvokeMethodResponse
import os
import maestro
import time
import logging

logging.basicConfig(level=logging.INFO)

logging.info('started order-processor')

app = App()

app_port = os.getenv('APP_PORT', '6002')

# Dapr subscription in /dapr/subscribe sets up this route
@app.method('orders')
def orders_subscriber(request: InvokeMethodRequest)-> InvokeMethodResponse:
    event = request.json
    print('Subscriber received : %s' % event.data['orderId'], flush=True)
    return InvokeMethodResponse(b'INVOKE_RECEIVED', "text/plain; charset=UTF-8")

@app.method('testRange')
def testRange_subscriber(request: InvokeMethodRequest)-> InvokeMethodResponse:
    logging.info('received testRange')
    servo =  maestro.Controller() #/dev/ttyACM1 or ttyACM0(default)

    channels = [0] #range(18)
    targets = [3000, 3500, 6500, 8000,9000,0] #[1,2000,3000,4000,6000,8000,9000]
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

@app.method('goTo')
def goTo_subscriber(request: InvokeMethodRequest)-> InvokeMethodResponse:
    event = request.json
    
    logging.info('received goTo')
    servo =  maestro.Controller() #/dev/ttyACM1 or ttyACM0(default)

    try:
        channelIndex = event.data["channelIndex"]
        accel = event.data["accel"]
        target = event.data["target"]
        logging.info(f'about to goTo channelIndex: {channelIndex} accel:{accel} target:{target}')
        #logging.info(f'min:{servo.getMin(channelIndex)} max:{servo.getMax(channelIndex)} pos:{servo.getPosition(channelIndex)} isMov:{servo.isMoving(channelIndex)} gMov:{servo.getMovingState()}')
        #servo.setSpeed(channelIndex,speed)
        servo.setAccel(channelIndex,accel)
        servo.setTarget(channelIndex,target)
    finally:
        logging.info('closing connection')
        servo.close()
    return InvokeMethodResponse(b'INVOKE_RECEIVED', "text/plain; charset=UTF-8")


app.run(app_port)

