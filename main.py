import uvicorn
from fastapi import FastAPI
from controller.Test01Controller import router as test01ControllerRouter
from controller.Test02Controller import router as test02ControllerRouter
from controller.Test03Controller import router as test03ControllerRouter
from loguru import logger

# 创建FastAPI实例
app = FastAPI()

# cros
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 注册全局中间件
@app.middleware("http")
async def add_test_filter(request, call_next):
    logger.info("处理前1")
    response = await call_next(request)
    logger.info("处理后1")
    return response

@app.middleware("http")
async def add_test_filter(request, call_next):
    logger.info("处理前2")
    response = await call_next(request)
    logger.info("处理后2")
    return response

# 注册路由
app.include_router(test01ControllerRouter)
app.include_router(test02ControllerRouter)
app.include_router(test03ControllerRouter)

if __name__ == "__main__":
    uvicorn.run("main:app",host="127.0.0.1",port=8000, reload=True)
