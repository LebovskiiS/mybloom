from pydantic import BaseModel


#schema for admin to fill and renew sort DB
class RequestSortSchema(BaseModel):
    name: str
    description: str
    color: str
    grow_time: str
    price: float
    min_unit_number: int
    class Config:
        from_attributes = True


class ResponseSortSchema(RequestSortSchema):
    id: int


class RequestUpdateSort(RequestSortSchema):
    id: int





