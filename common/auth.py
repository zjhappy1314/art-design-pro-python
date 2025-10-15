from typing import cast
from pydantic import BaseModel, Field

from fastapi import Request
from fastapi.routing import APIRoute

from common.exception import PermissionException
from common.permission_enum import MenuEnum, InterfaceEnum, ButtionEnum


class RoutePermission(BaseModel):
    ''' 路由权限类 '''
    menu_list: list[MenuEnum] = Field(default_factory=list, description='路由对应的菜单权限列表')
    interface_list: list[InterfaceEnum] = Field(default_factory=list, description='路由对应的接口权限列表')
    buttion_list: list[ButtionEnum] = Field(default_factory=list, description='路由对应的按钮权限列表')

    def to_openapi_extra(self) -> dict:
        return {self.get_extra_key(): self.model_dump()}
    
    @classmethod
    def get_extra_key(cls) -> str:
        return 'route_permission'
    
    def check_menu(self, code: str) -> bool:
        ''' 检查菜单权限 '''
        # 如果对应权限列表为空,表示对该权限不做限制,直接返回
        if not self.menu_list:
            return True
        return code in [item.value.code for item in self.menu_list]
    
    def chek_interface(self, code: str) -> bool:
        ''' 检查接口权限 '''
        # 如果对应权限列表为空,表示对该权限不做限制,直接返回
        if not self.interface_list:
            return True
        return code in [item.value.code for item in self.interface_list]
    
    def chek_button(self, code: str) -> bool:
        ''' 检查按钮权限 '''
        # 如果对应权限列表为空,表示对该权限不做限制,直接返回
        if not self.buttion_list:
            return True
        return code in [item.value.code for item in self.buttion_list]


def check_permission(request: Request):
    ''' 从请求中获取接口定义时附加的参数，判断是否允许访问
    权限分三种:菜单权限,接口权限和按钮权限
    '''
    # 获取当前路由的端点信息（包含定义时的参数）
    route: APIRoute = cast(APIRoute, request.scope.get('route'))
    print(route, '=========', route.openapi_extra)
    if not route or not route.openapi_extra:
        raise PermissionException('没有权限')
    
    route_permission = RoutePermission(**route.openapi_extra.get(RoutePermission.get_extra_key(), {}))
    print(route_permission.model_dump(), '==============')

    if not route_permission.check_menu('user-manage'):
        raise PermissionException('灭有权限')
