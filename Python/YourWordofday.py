from fastapi import APIRouter
from pydantic import BaseModel,Field
router = APIRouter()
class YourWordofdayInput(BaseModel):
    quest : str = Field(...,description="one word that you want to define your day; why; what does it mean to you?:")#quest = input(" one word that you want to define your day; why; what does it mean to you?:")
@router.post("/planongoodday")
def YourWordofday(user_input_YourWordofday:YourWordofdayInput):
    quest = user_input_YourWordofday.quest
    response = (
    f'This is a short reflection with that word {quest} as a motto'
    )
    {"response":response}