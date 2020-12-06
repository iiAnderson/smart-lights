import requests
import time
import json

from light_curve import get_curve
RELAY_URL = "http://192.168.0.63:3000/assistant"

def set_brightnesss_at(run_time, brightness, is_first=False):

    print(f"Setting Brightness {brightness} at {run_time}, currently {time.time()}")

    while True:
        current_time = time.time()

        if run_time <= current_time:
            set_brightness(brightness, is_first)
            break
            
        time.sleep(1)
    
    return True

def set_brightness(brightness, set_on=False):
    print(f"set robbie's lights to {round(brightness)}% brightness")
    r = requests.post(RELAY_URL, json={
        "command": f"set robbie's lights to {round(brightness)}% brightness",
        "broadcast": False,
        "user": "robbie"
    })

    print(r.reason)

    if set_on:
        requests.post(RELAY_URL, data=json.dumps({
            "command": f"turn on robbie's lights",
            "broadcast": False,
            "user": "robbie"
        }))


curve = get_curve(15, 0, 100)

for param in curve:
    set_brightnesss_at(param['time'], param['brightness'], is_first=param['is_first'])




