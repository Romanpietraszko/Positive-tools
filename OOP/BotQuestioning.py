import sys
sys.path.append("C:\\Users\\Acer\\Desktop\\Seriamałychapek\\Python")
import theplanongoodday
theplanongoodday.planongoodday()
class BotQuestioning:
    def Questions():
        bot_question1 = input("Chciałbym poprawić ci nastrój. Proszę wpisz 1 lub 2 abym mógł to zrobić: ")
        if bot_question1 == "1":
            theplanongoodday.planongoodday()
BotQuestioning.Questions()