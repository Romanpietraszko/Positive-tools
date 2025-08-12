from fastapi import APIRouter
from pydantic import BaseModel,Field
router = APIRouter()
class PositiveSloganofdayInput(BaseModel):
    quest1 : str = Field(...,description="What colors are calling you today?:")   #colors=input(" What colors are calling you today?:")  
    quest2 : str = Field(...,description="What gesture will you make for yourself today?")#gesture = input ("What gesture will you make for yourself today?")
    quest3 : str = Field(...,description="What motivational slogan are you adopting today?")#motivation = input("What motivational slogan are you adopting today?")
@router.post("/PositivesSloganofday")
def PositiveSloganofday(user_input_PositiveSloganofday:PositiveSloganofdayInput):
    colors = user_input_PositiveSloganofday.quest1
    gesture = user_input_PositiveSloganofday.quest2
    motivation = user_input_PositiveSloganofday.quest3
    response = (
        f' Today your outfit is in this color is {colors} but your powerful gesture is '
        f"{gesture},and you found motivation in the {motivation}."
        f"And this 3 elements are your your emotional and 'symbolic outfit of the day'"
    )
    {"response":response}