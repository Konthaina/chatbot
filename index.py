import gradio as gr
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

# Configure Gemini API key
genai.configure(api_key=os.getenv("GEMINI_API"))

# Load the Gemini model
model = genai.GenerativeModel(os.getenv("GEMINI_MODEL"))

conversation_history = []
# Define chat function
def chat(message, history):
    conversation_history.append({"role": "user", "parts": [message]})
    try:
        response = model.generate_content(conversation_history)  # fixed: generate_content (not generate_centent)
        conversation_history.append({"role": "model", "parts": [response.text]})
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# Create Gradio Chat Interface
demo = gr.ChatInterface(
    fn=chat,
    title="AngkorScience Chatbot",
    description="Ask me anything about AngkorScience!",
    examples=[
        "What is AngkorScience?",
        "Tell me about the research conducted at AngkorScience.",
        "How can I collaborate with AngkorScience?"
    ],
    theme="ocean",
    type="messages"
)

# Launch app
demo.launch(share=True)
