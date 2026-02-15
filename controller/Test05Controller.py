from datetime import datetime

from fastapi import APIRouter
from sqlalchemy import DateTime, func
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, JSON
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from sqlalchemy import select

router = APIRouter(tags=["test05"])

# 1. 定义基类
# DeclarativeBase简单来说，它的作用是充当一个“翻译官”和“注册表”，
# 将你定义的 Python 类（Class）与数据库中的表（Table）建立起映射关系
class Base(DeclarativeBase):
  create_time: Mapped[datetime] = mapped_column(DateTime,insert_default=func.now(),default=func.now,comment="创建时间")
  update_time:Mapped[datetime] = mapped_column(DateTime,insert_default=func.now(),onupdate=func.now(),default=func.now,comment="创建时间")

class User(Base):
  # 告诉 SQLAlchemy 映射到哪张表
  __tablename__ =  "user"
  id:Mapped[int] = mapped_column(primary_key=True)
  name:Mapped[str] = mapped_column(String(50),nullable=False)
  age:Mapped[int] = mapped_column(Integer,nullable=False)
  sex:Mapped[int] = mapped_column(Integer,nullable=False)
  cards:Mapped[list[str]] = mapped_column(JSON,nullable=False)
  is_delete:Mapped[int] = mapped_column(Integer,nullable=False)

def create_engine():
  # echo 打印sql
  return create_async_engine("mysql+aiomysql://root:Yang199691@yangyufan.top:3306/sqlalchemy",echo=True,pool_size=10,max_overflow=20)

async def create_table(engine = create_engine()):
    """创建数据库表"""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


AsyncSession = sessionmaker(
  bind = create_engine(), # 绑定数据引擎
  class_=AsyncSession, # 指定使用异步session
  expire_on_commit=False # 设置为False，避免session提交后对象被清空
)

async def get_database():
  async with AsyncSession() as session:
    try:
      yield session
      await session.commit()
    except Exception as e:
      await session.rollback()
      raise e
    finally:
      await session.close()

@router.get("/getUsers")
async def getUsers(db:AsyncSession = Depends(get_database)):
  result = await db.execute(select(User))
  return result.scalars().all()
