from dotenv import load_dotenv
import os
load_dotenv()
API_KEY = os.getenv("GEMINI_KEY")

from google import genai
client=genai.Client(api_key=API_KEY)
result=client.models.generate_content(model='gemini-3.5-flash',contents="is ronaldo better than messi in 20 words")
print(result.text)