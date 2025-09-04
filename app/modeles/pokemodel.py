from pydantic import BaseModel, Field
from typing import List

class Name(BaseModel):
    english: str = Field(..., example="Bulbasaur")
    japanese: str = Field(..., example="フシギダネ")
    chinese: str = Field(..., example="妙蛙种子")
    french: str = Field(..., example="Bulbizarre")

class Pokemon(BaseModel):
    id: int
    name: Name
    type: List[str] = Field(..., example=["Grass", "Poison"])
