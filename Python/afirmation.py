from pydantic import BaseModel, Field
from fastapi import APIRouter
router = APIRouter()
class AfirmationsInput(BaseModel):
    afirmation1: str = Field(...,description="How do you want to feel today?:")
    afirmation2: str = Field(...,description="What happend good or bad to you today?:")
    afirmation3: str = Field(..., description="What is your purpuse on today?:")     
@router.post("/afirmations")
def afirmations(user_input_afirmation:AfirmationsInput):
    afirmation1 = user_input_afirmation.afirmation1 #afirmation1 = input("How do you want to feel today?:")
    afirmation2 = user_input_afirmation.afirmation2 #afirmation2 = input("What happend good or bad to you today?:")
    afirmation3 = user_input_afirmation.afirmation3  #afirmation3 = input("What is your purpuse on today?:")
    response =( 
    f"This program is here to brighten your day.😇\n "
    f"Today you chose to  feel {afirmation1}. "
    f"Something meaningfull happend:{afirmation2}."
    f" Your purpuse today is:{afirmation3}"
    )
    return{"response":response}