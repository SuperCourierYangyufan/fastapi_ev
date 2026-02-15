import uvicorn
from fastapi import FastAPI, APIRouter
from controller.Test01Controller import router as test01ControllerRouter
from controller.Test02Controller import router as test02ControllerRouter
from controller.Test03Controller import router as test03ControllerRouter
from controller.Test04Controller import router as test04ControllerRouter
from controller.Test05Controller import router as test05ControllerRouter
from loguru import logger
from fastapi.middleware.cors import CORSMiddleware
from controller.Test05Controller import create_table

# 创建FastAPI实例
app = FastAPI(
    title="FastAPI 项目",
    description="基于 FastAPI 的后端服务",
    version="1.0.0"
)

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

@app.on_event("startup")
async def startup_event():
    await create_table()


# 注册路由
# 主应用
router = APIRouter(prefix='/api/v1')
# 其他业务
router.include_router(test01ControllerRouter)
router.include_router(test02ControllerRouter)
router.include_router(test03ControllerRouter)
router.include_router(test04ControllerRouter)
router.include_router(test04ControllerRouter)
router.include_router(test05ControllerRouter)
app.include_router(router)


if __name__ == "__main__":
    uvicorn.run("main:app",host="127.0.0.1",port=8000, reload=True)
