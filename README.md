# AI Dev Foundations

Foundational skills for building production-grade AI applications — covering LLM APIs, prompt engineering, reliability patterns and workflow automation.

## What This Repo Demonstrates

- **Working with LLM APIs directly** — Anthropic and OpenAI, including the structural differences between providers (message formatting, response parsing, parameter handling)
- **Prompt engineering for reliability** — structured (role/context/task/format) prompting, schema-enforced JSON output, and few-shot examples that generalize to unseen inputs
- **Production-ready Python patterns** — typed exception handling, retry logic with exponential backoff, and timeout handling for LLM API calls
- **Workflow automation with n8n** — webhook-triggered LLM calls, and a comparison build showing the difference between fixed-sequence automation and an autonomous AI Agent that dynamically selects tools
- **Manual agentic reasoning loops with LangGraph** — a hand-built ReAct-style tool-calling agent using conditional graph edges, alongside LangChain's prebuilt `create_agent` shortcut, demonstrating both the underlying mechanics and the production-ready API

## Repo Structure

| Folder | Focus |
|---|---|
| [`day1_llm_fundamentals`](./day1_llm_fundamentals) | Core LLM concepts: tokens, context windows, temperature/sampling, system vs. user prompts, agents vs. chatbots vs. automation |
| [`day2_first_api_calls`](./day2_first_api_calls) | First API integrations with Anthropic and OpenAI; provider-level structural differences |
| [`day3_prompt_engineering`](./day3_prompt_engineering) | Structured prompting, reliable JSON output, few-shot prompting |
| [`day4_python_patterns`](./day4_python_patterns) | Exception handling, retry logic with exponential backoff, timeout handling |
| [`day5_n8n_automation`](./day5_n8n_automation) | Webhook → LLM automation workflow, and an AI Agent workflow demonstrating autonomous tool selection |
| [`day6_agent_loops`](./day6_agent_loops) | A manually-built LangGraph agent loop (conditional edges, tool-calling), compared against LangChain's `create_agent` prebuilt shortcut |

## Key Technical Highlights

**Reliable structured output.** Enforcing JSON schemas in prompts and defensively parsing model output (stripping markdown code fences before `json.loads()`) to build a dependable extraction pipeline — see [`day3_prompt_engineering/structured_prompting.py`](./day3_prompt_engineering/structured_prompting.py).

**Generalization via few-shot prompting.** Two examples of compensation-type normalization were enough for the model to correctly classify an unseen "revenue-share" compensation structure — see [`day3_prompt_engineering/few_shot_prompting.py`](./day3_prompt_engineering/few_shot_prompting.py).

**Resilient API calls.** Differentiated retry logic that distinguishes transient failures (rate limits, connection errors — retried with exponential backoff) from permanent failures (authentication errors — raised immediately) — see [`day4_python_patterns/retry_logic.py`](./day4_python_patterns/retry_logic.py).

**Automation vs. agentic behavior.** Two n8n workflows in [`day5_n8n_automation`](./day5_n8n_automation) illustrate the distinction directly:
- `basic_automation_workflow.json` — a fixed, developer-defined sequence (Webhook → LLM call → Respond)
- `ai_agent_preview_workflow.json` — an AI Agent that autonomously decides whether and when to invoke a Calculator tool based on the input, rather than following a hardcoded path

**Hand-built vs. prebuilt agent loops.** [`day6_agent_loops/agent_loop.py`](./day6_agent_loops/agent_loop.py) implements a ReAct-style tool-calling loop manually using LangGraph's `StateGraph`, an explicit conditional edge function, and a loop-back edge — the same underlying mechanics that power [`day6_agent_loops/agent_shortcut.py`](./day6_agent_loops/agent_shortcut.py), which produces identical behavior using LangChain's `create_agent` prebuilt function in a fraction of the code.

## Stack

Python · Anthropic API · OpenAI API · n8n · LangChain · LangGraph · `python-dotenv`

## Related Projects

- [`support-triage-agent`](https://github.com/sravanibalne/support-triage-agent) — An autonomous AI agent that triages support emails, assesses priority, and drafts FAQ-grounded replies using n8n and the Anthropic API.
- [`pulseapi-docs-assistant`](https://github.com/sravanibalne/pulseapi-docs-assistant) — Code-first conversational AI chatbot (LangChain/LangGraph) for API documentation Q&A, with retrieval-augmented generation (Pinecone), a Streamlit demo, and a production-style FastAPI backend + embeddable chat widget.

## Author

Sravani Balne — Full Stack Developer / Tech Lead transitioning into AI development.
[LinkedIn](https://www.linkedin.com/in/sravanibalne/) · [GitHub](https://github.com/sravanibalne)