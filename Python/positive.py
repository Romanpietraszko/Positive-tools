from fastapi import APIRouter
from pydantic import BaseModel,Field
router = APIRouter()
class positiveInput(BaseModel):
    quest1 : str = Field(...,description="What was the smallest postive thing that happend to you?: ")#question1 = input("What was the smallest postive thing that happend to you?:")
    quest2 : str = Field(...,description="Could something simple, warm blanket or hot chocolate lift your spirits today? What other small comforts might help?:")#question2 =  input("Could something simple, warm blanket or hot chocolate lift your spirits today? What other small comforts might help?:")
    quest3 : str = Field(...,description="Did you know that after every storm, there's always a rainbow? What’s your rainbow today?")#question3 =  input("Did you know that after every storm, there's always a rainbow? What’s your rainbow today?")
@router.post("/positive")
def positive(user_input_positive : positiveInput):
    question1 = user_input.positive.quest1
    question2 = user_input.positive.quest2
    question3 = user_input.positive.quest3
    response =  (
        f"Before you start complaining about the struggles of your day, take a moment to notice what you haven't missed: {question1}.\n"
        f"If you're still stuck in negative thoughts, try imagining this-{question2} and feel it happening now.\n"
        f"There’s powerful positive energy hidden right here:{question3}"
        )
    {"response":response}