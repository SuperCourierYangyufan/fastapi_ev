from typing import Generic, TypeVar, Optional, Any
from pydantic import BaseModel

# 定义泛型变量
T = TypeVar('T')

# 创建三个独立的工厂函数
def _r_data(obj: Any = None):
    """
    返回数据成功响应
    :param obj: 要返回的数据对象
    :return: 响应对象,状态码200
    """
    return R(code=200, message="success", data=obj)

def _r_success(message: str = "操作成功"):
    """
    返回成功响应(无数据或空数据)
    :param message: 成功信息,默认为"操作成功"
    :return: 响应对象,状态码200
    """
    return R(code=200, message=message, data=None)

def _r_fail(message: str = "操作失败"):
    """
    返回失败响应
    :param message: 失败信息,默认为"操作失败"
    :return: 响应对象,状态码500
    """
    return R(code=500, message=message, data=None)

class RMeta(type(BaseModel)):
    """自定义元类,用于添加类方法"""
    
    @property
    def data(cls):
        """data属性返回_r_data函数"""
        return _r_data
    
    @property
    def success(cls):
        """success属性返回_r_success函数"""
        return _r_success
    
    @property
    def fail(cls):
        """fail属性返回_r_fail函数"""
        return _r_fail

class R(BaseModel, Generic[T], metaclass=RMeta):
    """
    统一响应结果类
    用于封装API返回数据
    """
    code: int
    message: str
    data: Optional[T] = None