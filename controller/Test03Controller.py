from entity.R import R
from entity.User import User
from fastapi import APIRouter, Request, Query
from fastapi.responses import FileResponse,StreamingResponse
from typing import List
from loguru import logger

router = APIRouter()

@router.post("/clientInfo")
async def clientInfo(request: Request):
    return {
        "ip": request.client.host,
        "port": request.client.port,
        "headers": dict(request.headers),
        "cookies": dict(request.cookies),
        "json": await request.json(),
        "form": await request.form(),
        "body": await request.body(),
    }


@router.get("/returnJson",
# 返回的对象,文档好看
response_model=R[User],
# 返回多个对象
# response_model=Union[User1,User2],
# 返回排除对象
response_model_exclude={"password","cards"},
# 去除空的返回显示
response_model_exclude_unset=True)
async def returnJson():
    user = User(id=1, name="test", age=18, sex=1, cards=["A"])
    return R.data(user)


@router.get("/getList",response_model=R[List[User]])
async def getList(sort : bool = Query(False,description="是否排序")):
    user1 = User(id=1, name="test", age=33, sex=1, cards=["A"])
    user2 = User(id=2, name="test2", age=21, sex=0, cards=["B"])
    user3 = User(id=3, name="test3", age=45, sex=1, cards=["C"])
    user4 = User(id=4, name="test4", age=66, sex=0, cards=["D"])
    list = [user1,user2,user3,user4]

    if(sort):
        list.sort(key=lambda x: x.age)

    logger.info(f"getList len:{len(list)}")  

    return R.data(list)

@router.get("/downFile")
async def downFile():
    return FileResponse(
        path="fastapi.pdf",
        filename="fastapi.pdf",
        media_type="application/pdf"
    )

@router.get("/streamDownFile")
async def streamDownFile():
    def generate_chunks(file_path: str,chunk_size: int = 1024 * 1024 * 1):
        with open(file_path,'rb') as f:
            while chunk := f.read(chunk_size):
                yield chunk
    return StreamingResponse(
        content=generate_chunks("fastapi.pdf"),
        media_type="application/pdf",
        filename="fastapi.pdf"
    )

@router.get("/",response_class=HTMLResponse)
