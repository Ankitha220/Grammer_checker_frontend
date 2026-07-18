import gradio as gr
import requests

API_URL = "https://grammer-checker-backend-zxey.onrender.com"

def grammar_checker(text):
    try:
        response = requests.post(API_URL, json={"text": text})

        if response.status_code == 200:
            data = response.json()

            if "corrected" in data:
                return data["corrected"]
            else:
                return data

        return response.text

    except Exception as e:
        return str(e)

demo = gr.Interface(
    fn=grammar_checker,
    inputs=gr.Textbox(
        lines=6,
        placeholder="Enter text here..."
    ),
    outputs=gr.Textbox(
        lines=6,
        label="Corrected Text"
    ),
    title="Grammar Checker using Gemini API",
    description="Correct grammar using Gemini."
)

demo.launch()
