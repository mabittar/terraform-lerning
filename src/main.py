from multiprocessing import context
from pathlib import Path
from typing import Any

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware


BASE_PATH = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "templates"))

origins = [
    "http://localhost",
    "http://localhost:8081",
    "http://localhost:8082",
]

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_main(request: Request) -> dict[str, str]:
    return {
        "message": "Hello World FastAPI",
        "root_path": request.scope.get("root_path"),
        "raw_url": str(request.url),
    }


@app.get("/html", response_class=HTMLResponse)
async def read_html(request: Request) -> Any:
    return TEMPLATES.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "message": "Hello World FastAPI",
            "root_path": request.scope.get("root_path"),
            "raw_url": str(request.url),
        },
    )


@app.get("/items/{item_id}")
async def read_item(item_id) -> dict[str, Any]:
    return {"item_id": item_id}
