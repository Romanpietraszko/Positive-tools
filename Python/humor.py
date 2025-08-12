from fastapi import APIRouter
from pydantic import BaseModel,Field
router = APIRouter()
class humorInput(BaseModel):
    quest1 : str = Field(...,description = "what made you laugh recently?:".lower())#question1 = input("what made you laugh recently?:".lower())
    quest2 : str = Field(..., description = 'what silly joke do you remember?:'.lower()) #question2 = input('what silly joke do you remember?:'.lower())
    quest3 : str = Field(..., description = "what would you say to someone to make them laugh?:".lower())#question3 = input("what would you say to someone to make them laugh?:".lower())
@router.post("/humor")    
def humor(user_input_humor:humorInput):
   question1 = user_input_humor.quest1
   question2 = user_input_humor.quest2 
   question3 = user_input_humor.quest3 
    response = (
        f"In summary of your own answers, it seems that '{question1}' gave you a proper laugh... "
        f"That joke you wrote: '{question2}' — honestly, it cracked me up too! But seriously, you should definitely say this out loud: '{question3}' — it could make someone’s day."
        )
    {"response":response}