from typing import Annotated
from fastapi import APIRouter,Form,File, UploadFile,HTTPException
from entity.User import User
import aiofiles


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
    # 分块读取并保存完整文件
    async with aiofiles.open("./" + file.filename, "wb") as buffer:
        # while True:
        #     chunk = await file.read(1024 * 1024)  # 读取1MB块
        #     if not chunk:
        #         break
        #     buffer.write(chunk)
        while chunk := await file.read(1024 * 1024):
            buffer.write(chunk)

    return {"filename": file.filename}

# 上传多个文件
@router.post("/batch-upload")
def batchUpload(files: list[UploadFile] = File(...)):
    return {"filenames": [file.filename for file in files]}

# 表单文件一起上传
@router.post("/uploadForm")
def uploadForm(file: UploadFile = File(...), username: str = Form(...)):
    return {"filename": file.filename, "username": username}

# 返回异常
@router.get("/error")
def error():
    raise HTTPException(status_code=401, detail="Something went wrong")