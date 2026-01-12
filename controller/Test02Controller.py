from typing import Annotated
from fastapi import APIRouter,Form,File, UploadFile
from entity.User import User

router = APIRouter()

@router.post("/form")
def form(username: str = Form(...,description="用户名",example="admin",min_length=3,max_length=10)
    , password: str = Form(...,description="密码",example="123456",min_length=6,max_length=12)):
    return {"username": username, "password": password}

@router.post("/form2")
def form2(user: Annotated[User,Form()]):
    return user

# 小文件
@router.post("/update")
def update(file: bytes=File(...)):
    return {"file_size": len(file)}

# 常用 大文件
@router.post("/uploadBig")
async def upload(file: UploadFile):
    # 异步读取
    contents = await file.read()
    return {"filename": file.filename}