from django.shortcuts import render
import datetime
from google import genai
import environ
import os

# Create your views here.

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, 'ai_Assistant/.env'))

environ.Env.read_env()
API_KEY = env("GEMINI_API_KEY")

messages = {}

def answer(user_message:str):
    ai_model = "gemini-2.0-flash"
    client = genai.Client(api_key=API_KEY)

    system_instruction = (
        "You are Gemini, an AI in this Django project. Act only as a simple AI chat assistant:\n"
        "- Answer in direct, plain text sentences.\n"
        "- Never use markdown formatting, code blocks (such as ```code or ```).\n"
        "- Only provide clear, plain answers to user questions.\n"
        "- If a question requires code or a special format, say “I can’t provide code or special formatting.”\n"
        "- If you do not know the answer, reply with “I don’t know.”"
    )

    response = client.models.generate_content(
        model=ai_model,
        contents=user_message
    )

    text = response.text or ""
    text = text.replace("```", "").replace("*", "")
    return text

def home_page(request):
    global messages

    if request.method == "POST":
        message = request.POST.get("message")

        if "send" in request.POST:
            messages[message] = answer(message)

            print(messages)



    return render(
        request,
        template_name="gemini/index.html",
        context={
            "messages":messages,
        }
    )