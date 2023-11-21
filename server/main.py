import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

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


STATIC_DIR = "../dist/"

if os.path.exists(STATIC_DIR):
    app.mount("/", StaticFiles(directory=STATIC_DIR, html=True), name="index")

    index_file = FileResponse(
        STATIC_DIR + "index.html", headers={"Cache-Control": "no-cache"}
    )

    @app.get("/", response_class=FileResponse)
    async def index():
        return index_file
