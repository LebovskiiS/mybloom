from pydantic import BaseModel, Field, constr
from typing import Optional

class MainSchema(BaseModel):
    pass


class CreatePlantSchema(MainSchema):
    name: str = constr(min_length=2, max_length=50)
    sort_id: int
    start_time: Optional[int]
    end_time: Optional[int]
    growing_on_percent: Optional[int]
    is_active: bool = Field(default= False)



class UpdatePlantSchema(MainSchema):
    farm_id: int
    sort_id: Optional[int]
    plants_name: str = constr(min_length=2, max_length=50)
    start_time: Optional[int]
    end_time: Optional[int]
    growing_on_percent: Optional[int]
    status: bool = Field(default= False)


class RequestPlantSchema(BaseModel):
    plant_id: Optional[int] = None



class PlantResponseSchema(BaseModel):
    id: int
    farm_id: int
    name: str
    sort_id: Optional[int] = None
    start_time: Optional[int] = None
    end_time: Optional[int] = None
    growing_on_percent: Optional[int] = None
    is_active: bool
    class Config:
        orm_mode = True
