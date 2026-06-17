import gradio as gr


def hello(name):
    return "Hello World"+ name + "!"


app = gr.Interface(
    fn=hello,
    inputs="text",
    outputs="text",
    title="EXAM GIT",
    description="Application Gradio basique",
)
if __name__ == "__main__":
     app.launch()
