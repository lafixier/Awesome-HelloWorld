#!/usr/bin/env python3

import os
import time
import threading
import psutil
import uvicorn
from fastapi import FastAPI

app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)

def killer():
    time.sleep(1)
    p = psutil.Process(os.getpid())
    p.kill()
    
@app.get("/")
async def hello():
    t = threading.Thread(target=killer)
    t.start()
    print("Hello World!!")
    return "Hello World!!"

uvicorn.run(app, host="127.0.0.1", port=8000)
