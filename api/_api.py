"""Module to setup fastapi API to expose API to the outside world."""
import logging
import random
from typing import Any, Dict
from starlette.datastructures import State
from fastapi import FastAPI
import uvicorn
import json

LOGGER = logging.getLogger("API")
logging.basicConfig(filename='file.log', filemode='w', level=logging.INFO)

app = FastAPI()

@app.get("/hello", status_code=200)
def post_resolved():
    with open('activities.json') as json_file:
        data = json.load(json_file)
    
    return data
    

def run(host: str, port: int) -> None:
    """Run the code challenge API."""
    uvicorn.run(app, host=host, port=port)
    
