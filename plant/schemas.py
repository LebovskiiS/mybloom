from pydantic import BaseModel, Field, constr
from typing import Optional

class MainSchema(BaseModel):
    pass


class CreatePlantSchema(MainSchema):
    farm_id: int
    name: str = constr(min_length=2, max_length=50)
    sort_id: Optional[int]
    start_time: Optional[int]
    end_time: Optional[int]
    total_weight: Optional[int]
    growing_on_percent: Optional[int]
    is_active: bool = Field(default= False)



class UpdatePlantSchema(MainSchema):
    farm_id: int
    sort_id: Optional[int]
    plants_name: str = constr(min_length=2, max_length=50)
    start_time: Optional[int]
    end_time: Optional[int]
    total_weight: Optional[int]
    growing_on_percent: Optional[int]
    status: bool = Field(default= False)