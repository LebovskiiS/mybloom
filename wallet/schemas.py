from pydantic import BaseModel, Field


class EditWallet(BaseModel):
    card_holder: str = Field(max_length= 255)
    card_number: str = Field(max_length= 16)
    card_exp_date: str = Field(max_length= 4)
    card_cvv: str = Field(max_length= 3)
    state: str = Field(max_length= 255)
    city: str = Field(max_length= 255)
    apartment: str = Field(max_length= 255)
    zip_code: str = Field(max_length= 255)