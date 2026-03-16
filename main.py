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
    return {"message": "It works good!"}

@app.get("/get_key")
async def get_key():
    return {"message": os.getenv("test_key1")}

@app.get("/get_key_2")
async def get_key():
    return {"message": os.getenv("test_key2")}

@app.get("/move_file")
async def move_file():
    src_bucket_name='jchuang_no_hierarchical'
    dst_bucket_name='jchuang_dst_bucket'
    storage_client = storage.Client()
    src_bucket = storage_client.bucket(src_bucket_name)
    dst_bucket = storage_client.bucket(dst_bucket_name)
    try:
        blob = src_bucket.blob('edulrs/_nonprocess/2025-09-03_pedia_1of1.zip')
        new_name = 'testcopy_permission/2025-09-03_pedia_1of1.zip'
        new_blob = src_bucket.copy_blob(blob, dst_bucket, new_name)
        return {"message": f"Copy {blob.name} to {new_name} Complete !" }
    except Exception as e:
        return {"message": f"Failed to trigger job: {e}"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)