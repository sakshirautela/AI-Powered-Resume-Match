import requests
import os
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def extract_skills_with_gemini(text):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": f"Extract only relevant technical and soft skills from this text. "
                                f"Return them as a comma-separated list.\n\n{text}"
                    }
                ]
            }
        ]
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        result = response.json()
        reply = result['candidates'][0]['content']['parts'][0]['text']
        skills = [s.strip() for s in reply.split(',') if s.strip()]
        return skills
    else:
        print("❌ Error:", response.text)
        return []
