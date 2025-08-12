from fastapi import APIRouter
from pydantic import BaseModel,Field
router = APIRouter()
class Good_news_of_dayInput(BaseModel):
    quest : str = Field(...,description="What good thing happened today in your life, your surroundings, the world?")#question = input("What good thing happened today in your life, your surroundings, the world?")
@router.post("/Good_news_of_day")    
def Good_news_of_day(user_input_Good_news_of_day:Good_news_of_dayInput):
    question = user_input_Good_news_of_day.quest
    response = (
    f"The good news in your life today was {question}"
    )
    {"response":response}