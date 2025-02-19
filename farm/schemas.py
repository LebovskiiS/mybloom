from pydantic import BaseModel, Field
from pydantic.config import ConfigDict


class FarmCreate(BaseModel):
    name: str = Field(max_length= 20)




class FarmUpdate(BaseModel):
    name: str = Field(max_length= 20)




class GetFarm(BaseModel):
    farm_id: int = Field(...)


class FarmDelete(BaseModel):
    farm_id: int = Field(...)



class FarmsResponse(BaseModel):
    id: int
    farm_name: str | None
    user_id: int

    model_config = ConfigDict(from_attributes=True)


