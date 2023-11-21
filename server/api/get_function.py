from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class Result(BaseModel):
    message: str


@router.get("/api/getFunction", response_model=Result)
def get_function():
    return {"message": "GET api is working"}
