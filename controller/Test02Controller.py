from typing import Annotated
from fastapi import APIRouter,Form
from entity.User import User

router = APIRouter()

@router.post("/form")
def form(username: str = Form(...,description="用户名",example="admin",min_length=3,max_length=10)
    , password: str = Form(...,description="密码",example="123456",min_length=6,max_length=12)):
    return {"username": username, "password": password}

@router.post("/form2")
def form2(user: Annotated[User,Form()]):
    return user
