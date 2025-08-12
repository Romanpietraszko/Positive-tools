from fastapi import APIRouter
from pydantic import BaseModel,Field
router = APIRouter()
class GoodnightInput(BaseModel):
    question : str=Field(..., description="How do you want to end this day, what will you set aside, and what will you not take to sleep?")
@router.post("/Goodnight")
def Goodnight(user_input_Goodnight:GoodnightInput):
    goodnight = user_input_Goodnight.question
    #goodnight = input("How do you want to end this day, what will you set aside, and what will you not take to sleep?")
    response = (
        f"Becouse before slept you left this - {goodnight}.This is your postive way to good sleep."
        )
    {"response":response}