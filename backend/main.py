
from fastapi import FastAPI
from dotenv import dotenv_values

from led import LedController

title = "RPi-ControlLED"
description = "This API controls an LED strip attached to a Raspberry Pi 3 Model B+"

init_config = dotenv_values(".env")
config = {key.lower() : int(value) for key, value in init_config.items()}

RED = config["red"]
BLUE = config["blue"]
GREEN = config["green"]

led = LedController(RED, BLUE, GREEN)

app = FastAPI(
    title=title, 
    description=description)


@app.get("/")
def say_hi():
    return {"Hello": "World"}

@app.get("/rgb")
def get_rgb():
    r, g, b = led.get_rgb()
    return { "red" : r , "green" : g , "blue" : b }

@app.post("/switch/{color}")
def switch(color: str):
    led.switch(config[color])

@app.post("/set/{color}")
def set_color(color: str, value: int):
    led.set_val(config[color], value)

@app.post("/rgb")
def set_rgb(r: int, g: int, b: int):
    led.set_val(RED, r)
    led.set_val(GREEN, g)
    led.set_val(BLUE, b)
    

@app.post("/turnoff")
def turn_off():
    led.turnoff()