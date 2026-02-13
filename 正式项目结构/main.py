import uvicorn
from fastapi import FastAPI, APIRouter

app = FastAPI()

v1_router = APIRouter(prefix='/api/v1')
user_router = APIRouter(prefix="user",tags=['用户'])
auth_router = APIRouter(prefix="auth",tags=['鉴权'])

v1_router.include_router(user_router)
v1_router.include_router(auth_router)

app.include_router(v1_router)

if __name__ == "__main__":
    uvicorn.run("main:app",host="127.0.0.1",port=8000, reload=True)
