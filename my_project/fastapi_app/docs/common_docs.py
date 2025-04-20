from pydantic import BaseModel
from typing import Generic, TypeVar, Optional
from pydantic.generics import GenericModel

T = TypeVar("T")


class SuccessResponse(GenericModel, Generic[T]):
    message: str
    data: Optional[T]


class ErrorResponse(BaseModel):
    message: str
    error_code: Optional[str] = None
