import os
from dotenv import load_dotenv
from anthropic import Anthropic

# Load API key from .env
load_dotenv()

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=20,
    temperature=0,
    system="You are a helpful assistant that explains things simply.",
    messages=[
        {"role": "user", "content": "Explain what an API is, in 2 sentences."}
    ]
)

print(response.content[0].text)