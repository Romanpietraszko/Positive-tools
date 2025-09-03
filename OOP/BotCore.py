import sys
import os
sys.path.append(os.path.dirname(__file__))
import streamlit as st
from positivebot import  BotTalking
from  BotQuestioning import Questions
# STREAMLIT UI
st.title("💬 Pozytywne Mikroapki")
st.image ("Copilot_positivetoolkit.png",caption="Gotowa do pomocy",use_column_width=True)
option = st.selectbox("Wybierz mikroapkę:", [
    "Afirmacja dnia",
    "Emotional Kit",
    "Good News",
    "Goodnight",
    "Gratitude Card",
    "Humor",
    "Positive Purposes",
    "Positive Energy",
    "Slogan of the Day",
    "Retrospection",
    "Plan on Good Day",
    "Word of the Day"
])

if option == "Afirmacja dnia":
    a1 = st.text_input("How do you want to feel today?")
    a2 = st.text_input("What happened (good or bad)?")
    a3 = st.text_input("What is your purpose today?")
    if st.button("Generuj afirmację"):
        st.write(Afirmations().generate(a1, a2, a3))

elif option == "Emotional Kit":
    q1 = st.text_input("What stresses you out?")
    q2 = st.text_input("What calms you down?")
    q3 = st.text_input("What sensory thing helps?")
    if st.button("Generuj zestaw emocjonalny"):
        st.write(EmotionalKit().generate(q1, q2, q3))

elif option == "Good News":
    news = st.text_input("What good thing happened today?")
    if st.button("Pokaż dobrą wiadomość"):
        st.write(GoodNews().generate(news))

elif option == "Goodnight":
    reflection = st.text_input("What will you leave behind before sleep?")
    if st.button("Zakończ dzień pozytywnie"):
        st.write(Goodnight().generate(reflection))

elif option == "Gratitude Card":
    gratitude = st.text_input("Who or what are you grateful for?")
    if st.button("Generuj kartę wdzięczności"):
        st.write(GratitudeCard().generate(gratitude))

elif option == "Humor":
    h1 = st.text_input("What made you laugh recently?")
    h2 = st.text_input("What silly joke do you remember?")
    h3 = st.text_input("What would you say to make someone laugh?")
    if st.button("Generuj humor"):
        st.write(Humor().generate(h1, h2, h3))

elif option == "Positive Purposes":
    p1 = st.text_input("One professional goal:")
    p2 = st.text_input("One social goal:")
    p3 = st.text_input("One personal goal:")
    if st.button("Generuj cele"):
        st.write(PositivePurposes().generate(p1, p2, p3))

elif option == "Positive Energy":
    e1 = st.text_input("Small positive thing today:")
    e2 = st.text_input("Comforting image or taste:")
    e3 = st.text_input("Your rainbow today:")
    if st.button("Generuj pozytywną energię"):
        st.write(PositiveEnergy().generate(e1, e2, e3))

elif option == "Slogan of the Day":
    s1 = st.text_input("What colors call you today?")
    s2 = st.text_input("What gesture will you make?")
    s3 = st.text_input("Your motivational slogan:")
    if st.button("Generuj slogan dnia"):
        st.write(PositiveSlogan().generate(s1, s2, s3))

elif option == "Retrospection":
    r1 = st.text_input("What went well yesterday?")
    r2 = st.text_input("What did you learn?")
    r3 = st.text_input("What would you improve?")
    if st.button("Generuj retrospekcję"):
        st.write(Retrospection().generate(r1, r2, r3))

elif option == "Plan on Good Day":
    plan = st.text_input("What will you do today for yourself, others, and peace?")
    if st.button("Generuj plan dnia"):
        st.write(PlanOnGoodDay().generate(plan))

elif option == "Word of the Day":
    word = st.text_input("One word to define your day:")
    if st.button("Generuj słowo dnia"):
        st.write(WordOfDay().generate(word))




                                                            