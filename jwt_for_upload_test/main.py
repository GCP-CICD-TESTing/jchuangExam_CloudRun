import logging
import time
from datetime import datetime
from typing import Optional

import google.cloud.logging
import jwt
import pytz
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

TZ = pytz.timezone("Asia/Taipei")


# cloud logging
client = google.cloud.logging.Client()
client.setup_logging()

logging.basicConfig(level=logging.INFO)
# logging.basicConfig(format="%(levelname)s:  %(message)s", level=logging.INFO)

app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Request(BaseModel):
    data_source: str
    bucket_name: str
    ttl: Optional[int] = 60 * 60


class Response(BaseModel):
    start_status: str = Field("start success", description="start status")


@app.post("/jwt-token", response_model=Response)
def jwt_token(item: Request):
    logging.info(f"request input: {item}")
    iat = int(time.time())
    exp = iat + item.ttl
    payload = {
        "aud": "https://uploadfile.jchuangtest.com",
        "iat": int(iat),
        "exp": int(exp),
        "bucket_key": item.data_source,
        "bucket_name": item.bucket_name,
    }

    signed_jwt = jwt.encode(
        payload,
        # data['private_key'],
        "yes",
        algorithm="HS256",
    )
    resp = {
        "jwt": signed_jwt,
        "created_date": datetime.now(TZ).isoformat(timespec="milliseconds"),
        "expired_date": datetime.fromtimestamp(exp, TZ).isoformat(timespec="milliseconds"),
    }
    logging.info(f"response output: {resp}")
    return JSONResponse(
        status_code=200,
        content=resp,
    )


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
