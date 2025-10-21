from enum import Enum


class GenderEnum(Enum):
    ''' 性别枚举类型 '''
    MALE = 'male'
    FEMALE = 'female'
    UNKNOWN = 'unknow'


class PermissionEnum(Enum):
    ''' 权限枚举类型 '''
    MENU = 'menu'
    BUTTON = 'button'
    INTERFACE = 'interface'
