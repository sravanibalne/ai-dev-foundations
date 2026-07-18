import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-4o-mini",
    max_tokens=200,
    temperature=0,
    messages=[
        {"role": "system", "content": "You are a helpful assistant that explains things simply."},
        {"role": "user", "content": "Explain what an API is, in 2 sentences."}
    ]
)

print(response.choices[0].message.content)