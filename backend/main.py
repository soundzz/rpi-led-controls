from typing import Union

from fastapi import FastAPI

title = """
        RPi-ControlLED
        """
description =   """
                This API controls an LED strip attached to a Raspberry Pi 3 Model B+
                """

app = FastAPI(
    title=title, 
    description=description)


@app.get("/")
def read_root():
    return {"Hello": "World"}
