import time
import os
from anthropic import APITimeoutError, Anthropic, APIError, APIConnectionError, RateLimitError, AuthenticationError
from dotenv import load_dotenv

load_dotenv()
client = Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY"),
    timeout=30.0  # seconds — give up waiting after 30s
    )

def call_claude_with_retry(prompt, max_retries=3):
    for attempt in range(1, max_retries + 1):
        try:
            response = client.messages.create(
                model="claude-sonnet-4-6",
                max_tokens=200,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.content[0].text

        except AuthenticationError:
            # Permanent failure — retrying won't help, stop immediately
            print("Invalid API key — check your credentials. Not retrying.")
            raise

        except RateLimitError:
            wait_time = 2 ** attempt  # exponential backoff: 2s, 4s, 8s...
            print(f"Rate limited. Attempt {attempt}/{max_retries}. Waiting {wait_time}s...")
            time.sleep(wait_time)

        except APIConnectionError:
            wait_time = 2 ** attempt
            print(f"Connection issue. Attempt {attempt}/{max_retries}. Waiting {wait_time}s...")
            time.sleep(wait_time)
            
        except APITimeoutError:
            wait_time = 2 ** attempt
            print(f"API timeout. Attempt {attempt}/{max_retries}. Waiting {wait_time}s...")
            time.sleep(wait_time)

    print("Max retries reached. Giving up.")
    return None

# Test it
result = call_claude_with_retry("Explain what an API is in one sentence.")
if result:
    print(result)