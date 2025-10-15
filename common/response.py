from pydantic import BaseModel
from typing import Any, Optional


class CommonResponse(BaseModel):
    code: int
    msg: Optional[str]
    data: Optional[Any]

    @classmethod
    def success(cls, msg: Optional[str] = None, data: Optional[Any] = None) -> 'CommonResponse':
        return CommonResponse(code=200, msg=msg, data=data)
    
    @classmethod
    def fail(cls, code: int = -1, msg: Optional[str] = None, data: Optional[Any] = None) -> 'CommonResponse':
        return CommonResponse(code=code, msg=msg, data=data)
