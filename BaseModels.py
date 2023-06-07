from pydantic import BaseModel

"""Request Body Structure"""
class Session(BaseModel):
    session_id: str
