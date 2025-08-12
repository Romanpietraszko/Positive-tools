from fastapi import APIRouter
from pydantic import BaseModel, Field
router = APIRouter()
class positive_purposesInput(BaseModel):
    quest1 : str=Field(...,description="What is your one profesional goal?:")#question1 = input("What is your one profesional goal?: ")
    quest2 : str=Field(...,description="What is your one social goal?:")#question2 = input("What is your one social goal?: ")
    quest3 : str=Field(...,description="What is your one personal goal?:")#question3 = input("What is your one personal goal?: ")
@router.post("/positive_purposes")
def positive_purposes(user_input_positive_purposes:positive_purposesInput):
    question1 = user_input_positive_purposes.quest1
    question2 = user_input_positive_purposes.quest2
    question3 = user_input_positive_purposes.quest3
    response = (
        "This is your plan on 3 small-wins today.\n"
        f"The first is:{question1}\n "
        f"the second is{question2}\n "
        f"the last is{question3}."
        )
    {"response":response}