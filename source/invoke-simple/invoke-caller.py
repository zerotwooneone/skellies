import json
import time
import logging

from dapr.clients import DaprClient

logging.basicConfig(level=logging.INFO)

with DaprClient() as d:
    req_data = {
        'id': 1,
        'message': 'hello world'
    }

    #while True:
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

    resp = d.invoke_method(
        'invoke-receiver',
        'goTo',
        data=json.dumps({
            'channelIndex': 1,
            'accel': 255,
            'target': 3000
        }),
    )

    resp = d.invoke_method(
        'invoke-receiver',
        'goTo',
        data=json.dumps({
            'channelIndex': 1,
            'accel': 255,
            'target': 0
        }),
    )