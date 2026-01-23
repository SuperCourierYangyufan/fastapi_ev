from pydantic import BaseModel, Field, field_validator
from entity.IsDeleteEnum import IsDeleteEnum

class User(BaseModel):
    # 必填,描述
    id: int = Field(...,description="用户唯一标识信息")
    # 默认值,最大长度,最小长度
    name: str = Field(default="YYF",max_length=10,min_length=2)
    # 必填,大于0,小于120
    age: int = Field(...,gt=0,lt=120)
    # 必填,正则表达式密码长度8-16
    password: str = Field(default="12345678", pattern= r"^.{8,16}$")
    # 自定义校验
    sex: int = Field(default=1) 
    @field_validator('sex')
    def sex_validator(cls, v):
        if v not in [0, 1]:
            raise ValueError('性别必须为0或1')
        return v
    # 列表最小长度,最大长度
    cards: list[str] = Field(default=["card1"], min_items=1, max_items=3)
    # 是否删除
    is_delete: IsDeleteEnum = Field(default=IsDeleteEnum.NO,description="是否删除,0:未删除,1:已删除")