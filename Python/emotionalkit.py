from fastapi import APIRouter
from pydantic import BaseModel, Field
router = APIRouter()
class EmotionalKitInput(BaseModel):
    emotionalkit1 : str = Field(...,description="what stresses you out?: ".lower())   
    emotionalkit2 : str = Field(..., description="what calms you down?: ".lower())
    emotionalkit3 : str = Field(....,description = "what music/image/taste helps?:".lower())
@router.post("/emotionalkit")
def emotionalkit(user_input_emotionalkit:EmotionalKitInput):
    question1  =  user_input_emotionalkit.emotionalkit1 #question1 = input(" what stresses you out?: ".lower())
    question2  =  user_input_emotionalkit.emotionalkit2 #question2 = input("what calms you down?: ".lower())
    question3  =  user_input_emotionalkit.emotionalkit3 #question3 = input("what music/image/taste helps?:".lower())
    response =(
    f"The reason your stress is {question1}.\n"
    f"So the emotional kit on this is :'{question2}+{question3}'"
    )
    {"response":response}