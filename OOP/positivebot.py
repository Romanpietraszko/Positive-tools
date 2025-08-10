class BotTalking:
    def Intro():
        user_answers = input("Hej😇!. Jak się dziś trzymasz?:")
        answers = ["dobrze" , "super" , "nieźle"]
        sadanswers = ["źle" , "niedobrze" , "średnio"]
        if user_answers in answers:
            print(" To super to słyszeć ale pamiętaj dzień może być jeszcze lepszy")
        elif user_answers in sadanswers:
            print("Po każdej burzy jest tęcza. Nabierz dystansu, odetchnij, i znajdź coś pozytwnego jeszcze w tym dniu :)")
BotTalking.Intro()
