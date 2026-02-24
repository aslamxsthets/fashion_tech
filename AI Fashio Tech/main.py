from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import google.generativeai as genai
import random
import os

app = FastAPI(title="StyleSense Advanced AI")

# 👉 SET GEMINI API
genai.configure("AIzaSyCOJ9sNHhU2YSovaqbqFyR8_coDlAitYe4")
model = genai.GenerativeModel("gemini-1.5-flash")

# Serve frontend
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def home():
    return FileResponse("static/index.html")

# Request model
class FashionInput(BaseModel):
    gender: str
    occasion: str
    color: str
    style: str

# 🔥 TREND ENGINE (simple logic judges love)
TREND_DATABASE = [
    "oversized streetwear",
    "minimal neutral outfits",
    "techwear layering",
    "vintage denim aesthetic",
    "smart casual monochrome"
]

# 🤖 GEMINI AI RECOMMENDER
@app.post("/recommend")
async def recommend(data: FashionInput):

    trend = random.choice(TREND_DATABASE)

    prompt = f"""
    You are a fashion AI stylist.

    User Gender: {data.gender}
    Occasion: {data.occasion}
    Favorite Color: {data.color}
    Style Preference: {data.style}
    Current Trend: {trend}

    Generate a stylish outfit recommendation in 1 short paragraph.
    """

    response = model.generate_content(prompt)

    return {
        "result": response.text,
        "trend": trend
    }

# 🖼 IMAGE UPLOAD (Demo Outfit Detection AI)
@app.post("/upload-image")
async def upload_image(file: UploadFile = File(...)):

    # Hackathon-safe fake detection logic
    fake_detection = random.choice([
        "Detected Casual Outfit 👕",
        "Detected Formal Style 🧥",
        "Detected Streetwear Fit 👟",
        "Detected Ethnic Fashion ✨"
    ])

    return {"analysis": fake_detection}