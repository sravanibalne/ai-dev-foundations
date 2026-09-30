import os
from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import SystemMessage
from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.prebuilt import ToolNode

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

tools = [lookup_error_code]

model = ChatAnthropic(
    model="claude-sonnet-4-6",
    temperature=0,
    anthropic_api_key=os.getenv("ANTHROPIC_API_KEY")
).bind_tools(tools)

def call_model(state: MessagesState):
    system = SystemMessage(content="You are a PulseAPI support assistant. Use the lookup_error_code tool when asked about error codes.")
    response = model.invoke([system] + state["messages"])
    return {"messages": response}

def should_continue(state: MessagesState):
    last_message = state["messages"][-1]
    if last_message.tool_calls:
        return "tools"
    return END

builder = StateGraph(MessagesState)
builder.add_node("call_model", call_model)
builder.add_node("tools", ToolNode(tools))

builder.add_edge(START, "call_model")
builder.add_conditional_edges("call_model", should_continue, {"tools": "tools", END: END})
builder.add_edge("tools", "call_model")

graph = builder.compile()

if __name__ == "__main__":
    result = graph.invoke({"messages": [{"role": "user", "content": "What does a 400 error mean?"}]})
    print(result["messages"][-1].content)