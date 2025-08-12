import sys
sys.path.append("C:\\Users\\Acer\\Desktop\\Seriamałychapek\\Python")
import theplanongoodday
import afirmation
import humor
import emotionalkit
import Good_news_of_day
import Goodnight
import GratituteCard
import positive_purposes
import positive
import PositiveSloganofday
import retrospection
import YourWordofday
from fastapi import APIRouter
from pydantic  import BaseModel
 router = APIRouter()
class BotQuestioning(BaseModel): 
    question : str = Field(...,description="Chciałbym poprawić ci nastrój. Proszę wpisz 1-12 abym mógł to zrobić: ")
@router.post("/Questions")
@staticmethod
def Questions(user_input_mood: BotQuestioning):
     question = user_input_question.question   #bot_questions = input("Chciałbym poprawić ci nastrój. Proszę wpisz 1-12 abym mógł to zrobić: ")
    if question == "1":
        theplanongoodday.planongoodday()
    elif question == "2":
        afirmation.afirmation()
    elif question == "3":
        humor.humor() 
    elif question == "4":
        emotionalkit.emotionalkit()
    elif question == "5":
        Good_news_of_day.Good_news_of_day() 
    elif question == "6":
        Goodnight.Goodnight() 
    elif question == "7":
        GratituteCard.GratituteCard() 
    elif question == "8":
        positive.positive() 
    elif question == "9":
        PositiveSloganofday.PositiveSloganofday() 
    elif question == "10":
        retrospection.retrospection() 
    elif question == "11":
        positive_purposes.positive_purposes() 
    elif question == "12":
        YourWordofday.YourWordofday()
    else:
        response =" Nie rozpoznonano numeru 1-12.Proszę wpisz wartość od 1 do 12:"    
    return {"response":response}