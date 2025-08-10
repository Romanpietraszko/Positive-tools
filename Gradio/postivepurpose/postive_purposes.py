import gradio as gr
def positive(question1,question2,question3):
    return f"This is your plan on 3 small-wins today.\nThe first is:{question1}\n the second is{question2}\n the last is{question3}."
question1 = gr.Textbox(label="What is your one profesional goal?: ")
question2 = gr.Textbox(label="What is your one social goal?: ")
question3 = gr.Textbox(label="What is your one personal goal?: ")

gr.Interface(
    fn = positive,
    inputs = [question1, question2, question3],
    outputs = "text",
).launch()
