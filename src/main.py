from typing import Any
from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
async def read_main(request: Request) -> dict[str, str]:
    return {
        "message": "Hello World FastAPI",
        "root_path": request.scope.get("root_path"),
        "raw_url": str(request.url),
    }

@app.get("/items/{item_id}")
async def read_item(item_id) -> dict[str, Any]:
    return {"item_id": item_id}