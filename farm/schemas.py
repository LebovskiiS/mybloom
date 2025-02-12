from pydantic import BaseModel, Field


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

    class Config:
        from_attributes = True

