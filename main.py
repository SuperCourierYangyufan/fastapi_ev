import uvicorn
from fastapi import FastAPI
from controller.Test01Controller import router as test01ControllerRouter
from controller.Test02Controller import router as test02ControllerRouter
from controller.Test03Controller import router as test03ControllerRouter

# 创建FastAPI实例
app = FastAPI()
# 注册路由
app.include_router(test01ControllerRouter)
app.include_router(test02ControllerRouter)
app.include_router(test03ControllerRouter)
if __name__ == "__main__":
    uvicorn.run("main:app",host="127.0.0.1",port=8000, reload=True)
