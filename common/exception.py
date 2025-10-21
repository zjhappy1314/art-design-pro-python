class ApiException(Exception):
    def __init__(self, *args: object) -> None:
        self.code = 500
        super().__init__(*args)


class PermissionException(Exception):
    ''' 权限校验异常 '''
    def __init__(self, *args: object) -> None:
        self.code = 401
        super().__init__(*args)
