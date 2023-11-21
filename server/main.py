from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api import get_function, post_function

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://127.0.0.1/",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(get_function.router)
app.include_router(post_function.router)
