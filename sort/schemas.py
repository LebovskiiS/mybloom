from pydantic import BaseModel


#schema for admin to fill and renew sort DB
class RequestSortSchema(BaseModel):
    name: str
    description: str
    color: str
    grow_time: int
    unit_weight: float
    price: float
    min_unit_number: float
    class Config:
        from_attributes = True


class ResponseSortSchema(RequestSortSchema):
    id: int


class RequestUpdateSort(RequestSortSchema):
    id: int





