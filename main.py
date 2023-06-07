from fastapi import FastAPI, Header
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from BaseModels import Session
from utilies import (
    api_response,
    create_jwt_token,
    verify_jwt_token
)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/create-session/")
async def set_user_gps(session: Session):
    session_id = session.session_id
    payload = {
        "session_id": session_id
    }
    token = create_jwt_token(payload)
    return JSONResponse(content=api_response(
        data={
            "token": token
        },
        message="Success",
        status_code=200
    ),
        status_code=200
    )


@app.get("/verify-session/")
async def verify_session(authorization: str = Header(...)):

    if not len(authorization.split(" ")) == 2:
        return JSONResponse(content=api_response(message="Prefix missing!",
                                                 status_code=400), status_code=400)

    if not authorization.split(" ")[0] == "Bearer":
        return JSONResponse(content=api_response(message="Invalid prefix!",
                                                 status_code=400), status_code=400)
    if verify_jwt_token(authorization.split(" ")[1]):
        return JSONResponse(content=api_response(message="Success!",
                                                 status_code=200), status_code=200)
    return JSONResponse(content=api_response(message="Invalid Token!",
                                                 status_code=400), status_code=400)

@app.get("/test-api/")
async def verify_session():
    return JSONResponse(content=api_response(message="Success!",
                                             status_code=200), status_code=200)
