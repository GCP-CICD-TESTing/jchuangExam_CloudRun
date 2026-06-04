from fastapi import FastAPI
import uvicorn
import os
from google.cloud import storage

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/test")
async def test():
    return {"message": "It works good! version = 20260604"}

@app.get("/get_key")
async def get_key():
    return {"message": os.getenv("test_key1")}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)