from fastapi import Header
from fastapi import Depends
from fastapi import APIRouter
from typing import Dict
from fastapi import HTTPException
from service.UserService import get_user_service,UserService

router = APIRouter()

def upper_str(str: str):
    return str.upper()

@router.get("/upper_str")
async def upper_str_async(result: str = Depends(upper_str)):
    return {"result": result}


def print_info(name:str,age:int) -> str:
    return f"name: {name}, age: {age}"


@router.get("/print_info")
async def print_info_async(param: dict = Depends(print_info)):
    return {"result": param}

def check_token(token: str = Header(...)):
    if(str(token) == "admin"):
        return true;
    raise HTTPException(status_code=401, detail="Something went wrong")

@router.get("/check_token",dependencies=[Depends(check_token)])
async def check_token_async():
    return {"result": token}


@router.get("/get_user")
async def get_user_async(id:int,user_service: UserService = Depends(get_user_service)):
    return user_service.get_user(id)
