# AFFIRMATIONS
class Afirmations:
    def generate(self, feel, happened, purpose):
        return (
            f"This program is here to brighten your day. 😇\n"
            f"Today you chose to feel: {feel}\n"
            f"Something meaningful happened: {happened}\n"
            f"Your purpose today is: {purpose}"
        )

# EMOTIONAL KIT
class EmotionalKit:
    def generate(self, stress, calm, sensory):
        return (
            f"The reason your stress is: {stress}\n"
            f"So the emotional kit on this is: '{calm} + {sensory}'"
        )

# GOOD NEWS
class GoodNews:
    def generate(self, news):
        return f"The good news in your life today was: {news}"

# GOODNIGHT
class Goodnight:
    def generate(self, reflection):
        return f"Because before sleep you left this: {reflection}. This is your positive way to good sleep."

# GRATITUDE
class GratitudeCard:
    def generate(self, gratitude):
        return f"I'm grateful for: {gratitude}"

# HUMOR
class Humor:
    def generate(self, laugh, joke, message):
        return (
            f"In summary: '{laugh}' gave you a proper laugh.\n"
            f"That joke: '{joke}' — cracked me up too!\n"
            f"Say this out loud: '{message}' — it could make someone’s day."
        )

# POSITIVE PURPOSES
class PositivePurposes:
    def generate(self, goal1, goal2, goal3):
        return (
            f"This is your plan for 3 small wins today:\n"
            f"1. {goal1}\n2. {goal2}\n3. {goal3}"
        )

# POSITIVE ENERGY
class PositiveEnergy:
    def generate(self, small_thing, comfort, rainbow):
        return (
            f"Notice what you haven't missed: {small_thing}\n"
            f"Imagine this: {comfort}\n"
            f"Your rainbow today: {rainbow}"
        )

# SLOGAN OF THE DAY
class PositiveSlogan:
    def generate(self, colors, gesture, motivation):
        return (
            f"Today your outfit color is: {colors}\n"
            f"Your powerful gesture: {gesture}\n"
            f"Motivation: {motivation}\n"
            f"These 3 elements are your emotional and symbolic outfit of the day."
        )

# RETROSPECTION
class Retrospection:
    def generate(self, good, learned, improve):
        return (
            f"Yesterday went well: {good}\n"
            f"You learned: {learned}\n"
            f"You would improve: {improve}\n"
            f"This is your inspiring note: 'From yesterday for today'"
        )

# PLAN ON GOOD DAY
class PlanOnGoodDay:
    def generate(self, plan):
        return f"So your plan for a good day is: {plan}"

# WORD OF THE DAY
class WordOfDay:
    def generate(self, word):
        return f"This is a short reflection with the word '{word}' as your motto."




