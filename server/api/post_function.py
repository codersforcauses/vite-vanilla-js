from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class Input(BaseModel):
    text: str


class Result(BaseModel):
    message: str


@router.post("/api/postFunction", response_model=Result)
def post_function(data: Input):
    return {"message": f'POST api is working, received "{data.text}"'}
