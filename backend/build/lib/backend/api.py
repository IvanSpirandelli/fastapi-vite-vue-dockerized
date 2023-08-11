import random
import uvicorn

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

PORT = 1071

app = FastAPI()

origins = [
    "http://localhost:8080",
    "http://0.0.0.0:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def index():
    return {"message": "Is this a web app?"}

@app.get("/get_random_message")
def get_random_message():
    messages = [
        "Ants are nuts.", 
        "Berlin is like a doughnut.", 
        "Nothing isn't.", 
        "Some memes make me snort."
        ]
    return {"message": messages[random.randint(0, len(messages) - 1)]}

if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=PORT, debug=True, reload=True)
