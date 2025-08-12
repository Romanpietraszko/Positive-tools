from fastapi import APIRouter
from pydantic import BaseModel,Field
router = APIRouter()
class RetrospectionInput(BaseModel):
    quest1 : str = Field(...,description="what went well yesterday?: ".lower()) #question1 = input ("what went well yesterday?: ".lower())
    quest2 : str = Field(...,description="what did you learn?: ".lower())#question2 = input ("what did you learn?: ".lower())
    quest3 : str = Field(...,description="what would you improve?:".lower())#question3 = input ("what would you improve?:".lower())
@router.post("/retrospection")
def retrospection(user_input_retrospection:RetrospectionInput):
    question1 = user_input_PositiveSloganofday.quest1
    question2 = user_input_PositiveSloganofday.quest2
    question3 = user_input_PositiveSloganofday.quest3
    response = (
    f"Yesterday you went well this:{question1}\n after this you learnt this{question2}\n"
    f" and you would improve this: {question3}.\n"
    "This is  inspiring note in the style of 'From yesterday for today'"
    )
    {"response":response}