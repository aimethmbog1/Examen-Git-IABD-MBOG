import gradio as gr


def hello():
    return "Hello World"


app = gr.Interface(
    fn=hello,
    inputs=[],
    outputs="text",
    title="EXAM GIT",
    description="Application Gradio basique",
)

app.launch()
