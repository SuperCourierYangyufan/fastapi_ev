from enum import Enum

class IsDeleteEnum(int, Enum):
    """是否删除枚举"""
    NO = 0  # 未删除
    YES = 1  # 已删除
