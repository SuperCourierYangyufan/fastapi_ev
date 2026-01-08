from fastapi import APIRouter, Path
from typing import Optional, Annotated
from pydantic import BeforeValidator
from entity.User import User

router = APIRouter()

@router.get("/hello")
def hello():
    return {"message": "Hello World"}

@router.get("/hello/{name}/{age}")
# Path参数,只有路径参数使用
# ... 表示必填
# lt 表示小于
# gt 表示大于
def hello1(name: str = Path(...), age: int = Path(..., lt=100, gt=18)):
    return {"message": f"Hello {name}, {age}"}

@router.get("/query")
def hello2(name: Optional[str] = "yyf"):  
    return {"message": f"Hello {name}"}

@router.post("/user")
def create_user(user: User):
    print(user)
    return user;

def checkName(value: str):
    if value != "yyf":
        raise ValueError("name must be yyf")
    return value

@router.get("/check")
def hello3(name: Annotated[str, BeforeValidator(checkName)]):
    return {"message": f"Hello {name}"}

@router.get("fieldCheck")
def fieldCheck(user: User):
    return user