from pydantic import BaseModel, Field
from typing import List

class Name(BaseModel):
    english: str = Field(..., example="Bulbasaur")
    japanese: str = Field(..., example="フシギダネ")
    chinese: str = Field(..., example="妙蛙种子")
    french: str = Field(..., example="Bulbizarre")

class BaseStats(BaseModel):
    HP: int = Field(..., example=45)
    Attack: int = Field(..., example=49)
    Defense: int = Field(..., example=49)
    Sp_Attack: int = Field(..., alias="Sp. Attack", example=65)
    Sp_Defense: int = Field(..., alias="Sp. Defense", example=65)
    Speed: int = Field(..., example=45)

class Pokemon(BaseModel):
    id: int
    name: Name
    type: List[str] = Field(..., example=["Grass", "Poison"])
    base: BaseStats