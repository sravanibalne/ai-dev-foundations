import os
from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_anthropic import ChatAnthropic
from langchain.agents import create_agent

load_dotenv()

@tool
def lookup_error_code(code: str) -> str:
    """Look up what a PulseAPI HTTP error code means. Input should be a numeric code like '429' or '500'."""
    error_codes = {
        "400": "Invalid request body or missing required field",
        "401": "Invalid or missing API key",
        "404": "Template ID not found",
        "429": "Rate limit exceeded",
        "500": "Internal server error — safe to retry with backoff"
    }
    return error_codes.get(code, f"Unknown error code: {code}")

model = ChatAnthropic(
    model="claude-sonnet-4-6",
    temperature=0,
    anthropic_api_key=os.getenv("ANTHROPIC_API_KEY")
)

agent = create_agent(
    model=model,
    tools=[lookup_error_code],
    system_prompt="You are a PulseAPI support assistant. Use the lookup_error_code tool when asked about error codes."
)

if __name__ == "__main__":
    result = agent.invoke({"messages": [{"role": "user", "content": "What does a 429 error mean?"}]})
    print(result["messages"][-1].content)