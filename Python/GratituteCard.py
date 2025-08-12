from fastapi import APIRouter
from pydantic import BaseModel,Field
router = APIRouter()
class GratituteCardInput(BaseModel):
    quest : str=Field(...,description="Who are you grateful for today, for what, and how can you express it?:")#question = input("Who are you grateful for today, for what, and how can you express it?:")
@router.post("/GratituteCard")    
def GratituteCard(user_input_GratituteCard:GratituteCardInput):
    question = user_input_GratituteCard.quest
    response = (
        f"Im gratitute for: {question}"
        )
    {"response":response}