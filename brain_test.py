
import time
from dotenv import load_dotenv
from google import genai
from google.genai import errors

load_dotenv()
client = genai.Client()

models = ["gemini-3.8-flash", "gemini-3.5-flash-lite", "gemini-3.6-flash"]
question = "Explain what an AI agent is in one sentence."
answered = False

for model in models:
    try:
        response = client.models.generate_content(model=model, contents=question)
        print("Answered by " + model + ":")
        print(response.text)
        answered = True
        break
    except errors.APIError as e:
        print(model + " failed: " + str(e)[:40])
        time.sleep(2)

if not answered:
    print("All models are busy right now. Try again in a few minutes.")