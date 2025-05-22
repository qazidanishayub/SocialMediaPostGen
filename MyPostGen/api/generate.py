from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import google.generativeai as genai

app = FastAPI()

# Allow frontend to access API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-001")

class PostRequest(BaseModel):
    user_idea: str
    domain: str

@app.post("/generate")
def generate_post(data: PostRequest):
    prompt = f'''
You are a LinkedIn strategist helping a tech expert write a post about: {data.domain}.
User input (if any): {data.user_idea}

Generate a post (250–350 words) with:
- Strong hook
- Problem/opportunity
- Solution or analogy
- User expertise & tools
- CTA & relevant hashtags

Make it readable, professional, and engaging.
'''
    response = model.generate_content(prompt)
    return { "post": response.text.strip() }
