import json
import time
import logging
import asyncio

from dapr.clients import DaprClient

logging.basicConfig(level=logging.INFO)

async def onInvoke(d: DaprClient) -> asyncio.coroutine:
    channelIndex = 0
    accel = 0 #zero is unrestricted, just use speed
    speed = 240 #60 generally means full range takes 1 second, 1 means full range takes 1 minute
    
    resp = await d.invoke_method_async(
        'invoke-receiver',
        'goTo',
        data=json.dumps({
            'channelIndex': channelIndex,
            'accel': accel,
            'target': 6000,
            #'speed': speed
        }),
    )
    # Print the response
    print(resp.content_type, flush=True)
    print(resp.text(), flush=True)
    print(str(resp.status_code), flush=True)

    time.sleep(5)
    
    resp = await d.invoke_method_async(
        'invoke-receiver',
        'goTo',
        data=json.dumps({
            'channelIndex': channelIndex,
            #'accel': accel,
            'target': 9000,
            #'speed': speed
        }),
    )
    # Print the response
    print(resp.content_type, flush=True)
    print(resp.text(), flush=True)
    print(str(resp.status_code), flush=True)

    time.sleep(5)

    resp = await d.invoke_method_async(
        'invoke-receiver',
        'goTo',
        data=json.dumps({
            'channelIndex': channelIndex,
            #'accel': accel,
            'target': 3000,
            #'speed': speed
        }),
    )
    # Print the response
    print(resp.content_type, flush=True)
    print(resp.text(), flush=True)
    print(str(resp.status_code), flush=True)

with DaprClient() as d:
    """
    req_data = {
        'id': 1,
        'message': 'hello world'
    }

    
    while True:
        # Create a typed message with content type and body
        resp = d.invoke_method(
            'invoke-receiver',
            'my-method',
            data=json.dumps(req_data),
        )
        
        # Print the response
        print(resp.content_type, flush=True)
        print(resp.text(), flush=True)
        print(str(resp.status_code), flush=True)
        
        time.sleep(2)
    """

    asyncio.run(onInvoke(d))