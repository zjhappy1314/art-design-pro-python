from sqlalchemy import Column, Integer, ForeignKey

from db import DBBaseModel


class RolePermissionModel(DBBaseModel):
    ''' 角色权限模型 '''
    __tablename__ = 'role_permission'

    rid = Column(Integer, ForeignKey('role.id'), comment='角色ID')
    pid = Column(Integer, ForeignKey('permission.id'), comment='权限ID')
