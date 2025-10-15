from enum import Enum
from typing import Union
from fastapi import APIRouter
from pydantic import BaseModel, ConfigDict

from .user import router as user_router


class RouteInfo(BaseModel):
    prefix: str
    router: APIRouter
    tags: list[Union[str, Enum]]

    # 允许任意类型,解决router类型报错问题
    model_config = ConfigDict(arbitrary_types_allowed=True)


router_list: list[RouteInfo] = [
    RouteInfo(prefix='/users', router=user_router, tags=['user']),
]

__all__ = ['router_list']
