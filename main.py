from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from dotenv import load_dotenv, find_dotenv
from presentation.controllers import tasks_controller
import os

load_dotenv(find_dotenv())



USER = os.environ.get("USER_DB")
PASSWORD = os.environ.get("PASSWORD_DB")
CLUSTER = os.environ.get("CLUSTER_DB")

app = FastAPI()

origins = [
    "http://localhost:5173/",
    "http://0.0.0.0:5173/",
    "http://localhost:5173",
    "http://0.0.0.0:5173",
    "https://tasks-todo-six.vercel.app/",
    "https://tasks-todo-six.vercel.app"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rotas e Controllers
app.include_router(tasks_controller.routes)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)