from pydantic import BaseModel, Field


class FarmCreate(BaseModel):
    name: str = Field(max_length= 20)
    land_size: int
    plants_id: int = Field(default= None)


class FarmUpdate(BaseModel):
    name: str = Field(max_length= 20)
    land_size: int
    plants_id: int = Field(default= None)

class GetFarm(BaseModel):
    farm_id: int = Field(...)


class FarmDelete(BaseModel):
    farm_id: int = Field(...)


