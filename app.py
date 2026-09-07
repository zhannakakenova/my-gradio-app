import gradio as gr


def greet(name):
    return f"Hello, {name}! CI/CD is working 🚀"


demo = gr.Interface(
    fn=greet,
    inputs=gr.Textbox(label="Your name"),
    outputs=gr.Textbox(label="Result"),
    title="My First CI/CD Gradio App",
    description="Deployed automatically with GitHub Actions and Hugging Face Spaces."
)


if __name__ == "__main__":
    demo.launch()
