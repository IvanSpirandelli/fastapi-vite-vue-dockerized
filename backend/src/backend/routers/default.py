import random
from fastapi import APIRouter, Depends

default_router = APIRouter(
    prefix="",
    tags=["default"],
    responses={404: {"description": "Not found"}},
)

@default_router.get("/")
def index():
    return {"message": "Is this a web app?"}

@default_router.get("/get_random_message")
def get_random_message():
    messages = [
        "Ants are nuts.", 
        "Berlin is like a doughnut.", 
        "Nothing isn't.", 
        "Some memes make me snort."
        ]
    return {"message": messages[random.randint(0, len(messages) - 1)]}