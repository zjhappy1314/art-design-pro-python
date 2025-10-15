from fastapi import APIRouter

from common.auth import RoutePermission
from common.response import CommonResponse
from common.permission_enum import MenuEnum, InterfaceEnum, ButtionEnum

import services.user as UserService


router = APIRouter()

@router.get('/', openapi_extra=RoutePermission(
        menu_list=[MenuEnum.USER_MANAGE],
        interface_list=[InterfaceEnum.USER_GET]
).to_openapi_extra())
async def get():
    return CommonResponse.success('没问题', {'temp': UserService.get_list()})
