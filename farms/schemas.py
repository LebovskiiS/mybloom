from pydantic import BaseModel, Field


class FarmCreate(BaseModel):
    user_id: int = Field(...)
    name: str = Field(max_length= 20)
    land_size: int
    plants_id: int = Field(default= None)


class FarmUpdate(BaseModel):
    name: str = Field(max_length= 20)
    land_size: int
    plants_id: int = Field(default= None)


class FarmDelete(BaseModel):
    farm_id: int = Field(...)


class FarmAddPlants(BaseModel):
    user_id: int = Field(...)
    farm_id: int = Field(...)
