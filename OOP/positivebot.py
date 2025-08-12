from  fastapi import APIRouter
from pydantic import BaseModel
class BotTalking(BaseModel):
    mood: str=Field(...,description="Hej😇!. Jak się dziś trzymasz?:")")
    router = APIRouter()
@router.get("/Intro")
def Intro(user_input_mood:BotTalking(BaseModel)):
        #user_answers = input("Hej😇!. Jak się dziś trzymasz?:")
    mood = user_input_mood
    answers = ["dobrze" , "super" , "nieźle"]
    sadanswers = ["źle" , "niedobrze" , "średnio"]
    if user_answers in answers:
        print(" To super to słyszeć ale pamiętaj dzień może być jeszcze lepszy")
    elif user_answers in sadanswers:
        print("Po każdej burzy jest tęcza. Nabierz dystansu, odetchnij, i znajdź coś pozytwnego jeszcze w tym dniu :)")

return{"response":response}