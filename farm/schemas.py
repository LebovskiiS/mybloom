from pydantic import BaseModel, Field


class FarmCreate(BaseModel):
    name: str = Field(max_length= 20)
    land_size: int




class FarmUpdate(BaseModel):
    name: str = Field(max_length= 20)
    land_size: int




class GetFarm(BaseModel):
    farm_id: int = Field(...)


class FarmDelete(BaseModel):
    farm_id: int = Field(...)



class FarmsResponse(BaseModel):
    id: int
    farm_name: str | None
    land_size: int | None
    user_id: int


    class Config:
        from_attributes = True

