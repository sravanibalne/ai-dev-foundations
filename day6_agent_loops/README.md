# Day 6 — Manual Agent Loops (LangGraph)

A hands-on deep dive into how tool-calling agents actually work under the hood, going beyond using a prebuilt agent function.

## Files

- **`agent_loop.py`** — A manually-built ReAct-style agent loop using LangGraph's `StateGraph`, with an explicit conditional edge (`should_continue`) that routes between a model-calling node and a tool-execution node based on whether the model requested a tool call. Demonstrates the actual reason → act → observe loop that underlies all tool-calling agents.
- **`agent_shortcut.py`** — The same agent, rebuilt using `create_agent` from `langchain.agents` — LangChain's current prebuilt shortcut that automates the conditional graph shown in `agent_loop.py`. Produces identical behavior with significantly less code.
- **`test_retrieval.py`** — A standalone script for testing Pinecone vector search in isolation, used while building RAG for the [`pulseapi-docs-assistant`](https://github.com/sbalne/pulseapi-docs-assistant) project — verifying semantic retrieval quality before wiring it into the full chatbot.

## Why Build It Manually First

Using a prebuilt agent function like `create_agent` is the right choice for real project work, but understanding the underlying mechanics — the conditional routing logic that decides "call a tool" vs. "give a final answer" — is what distinguishes genuine hands-on LangChain/LangGraph experience from simply calling a high-level API. `agent_loop.py` and `agent_shortcut.py` together demonstrate both: the ability to build the loop from scratch, and the judgment to use the shortcut when custom routing logic isn't needed.
