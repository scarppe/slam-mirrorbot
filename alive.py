# Implement By - @anasty17 (https://github.com/SlamDevs/slam-mirrorbot/commit/0bfba523f095ab1dccad431d72561e0e002e7a59)
# (c) https://github.com/SlamDevs/slam-mirrorbot
# All rights reserved

import time
import requests
import os

global PING_INTERVAL
BASE_URL = os.environ.get('BASE_URL_OF_BOT', None)
try:
    if len(BASE_URL) == 0:
        BASE_URL = None
    PING_INTERVAL = int(os.environ.get('PING_INTERVAL')) * 60
except:
    BASE_URL = None
    PING_INTERVAL = 600
PORT = os.environ.get('PORT', None)
if PORT is not None and BASE_URL is not None:
    while True:
        time.sleep(PING_INTERVAL)
        status = requests.get(BASE_URL).status_code
