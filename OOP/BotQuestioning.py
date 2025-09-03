from microapps import (
    Afirmations,
    Humor,
    Retrospection,
    EmotionalKit,
    GoodNews,
    Goodnight,
    GratitudeCard,
    PositiveEnergy,
    PositiveSlogan,
    PositivePurposes,
    PlanOnGoodDay,
    WordOfDay
)

class Questions:
    def handle(self, number: str, inputs: list):
        if number == "1":
            return PlanOnGoodDay().generate(inputs[0])
        elif number == "2":
            return Afirmations().generate(inputs[0], inputs[1], inputs[2])
        elif number == "3":
            return Humor().generate(inputs[0], inputs[1], inputs[2])
        elif number == "4":
            return EmotionalKit().generate(inputs[0], inputs[1], inputs[2])
        elif number == "5":
            return GoodNews().generate(inputs[0])
        elif number == "6":
            return Goodnight().generate(inputs[0])
        elif number == "7":
            return GratitudeCard().generate(inputs[0])
        elif number == "8":
            return PositiveEnergy().generate(inputs[0], inputs[1], inputs[2])
        elif number == "9":
            return PositiveSlogan().generate(inputs[0], inputs[1], inputs[2])
        elif number == "10":
            return Retrospection().generate(inputs[0], inputs[1], inputs[2])
        elif number == "11":
            return PositivePurposes().generate(inputs[0], inputs[1], inputs[2])
        elif number == "12":
            return WordOfDay().generate(inputs[0])
        else:
            return "Nie rozpoznano numeru. Wpisz wartość od 1 do 12."
