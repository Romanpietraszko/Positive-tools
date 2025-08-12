from fastapi import APIRouter
from pydantic import BaseModel,Field
router = APIRouter()
class PlanongooddayInput(BaseModel):
    quest1 : str = Field(...,description="What will you do today for yourself, for others, and for peace?:")#odpowiedz = input("What will you do today for yourself, for others, and for peace?:") 
@router.post("/planongoodday")
def planongoodday(user_input_planongoodday:PlanongooddayInput):
    odpowiedz = user_input_planongoodday.quest1
    response = (
    f"So your plan on good day is. For yourself for others and for peace you will do this: {odpowiedz}"
    )
    {"response":response}