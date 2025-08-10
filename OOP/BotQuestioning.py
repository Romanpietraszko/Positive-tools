import sys
sys.path.append("C:\\Users\\Acer\\Desktop\\Seriamałychapek\\Python")
import theplanongoodday
import afirmation
import humor
class BotQuestioning(): 
    @staticmethod
    def Questions():
        bot_question1 = input("Chciałbym poprawić ci nastrój. Proszę wpisz 1,2 lub 3 abym mógł to zrobić: ")
        if bot_question1 == "1":
            theplanongoodday.planongoodday()
        elif bot_question1 == "2":
            afirmation.afirmation()
        elif bot_question1 == "3":
            humor.humor()
        
BotQuestioning.Questions()