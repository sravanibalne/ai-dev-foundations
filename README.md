# AI Dev Foundations

Foundational skills for building production-grade AI applications — covering LLM APIs, prompt engineering, reliability patterns and workflow automation.

## What This Repo Demonstrates

- **Working with LLM APIs directly** — Anthropic and OpenAI, including the structural differences between providers (message formatting, response parsing, parameter handling)
- **Prompt engineering for reliability** — structured (role/context/task/format) prompting, schema-enforced JSON output, and few-shot examples that generalize to unseen inputs
- **Production-ready Python patterns** — typed exception handling, retry logic with exponential backoff, and timeout handling for LLM API calls
- **Workflow automation with n8n** — webhook-triggered LLM calls, and a comparison build showing the difference between fixed-sequence automation and an autonomous AI Agent that dynamically selects tools

## Repo Structure

| Folder | Focus |
|---|---|
| [`day1_llm_fundamentals`](./day1_llm_fundamentals) | Core LLM concepts: tokens, context windows, temperature/sampling, system vs. user prompts, agents vs. chatbots vs. automation |
| [`day2_first_api_calls`](./day2_first_api_calls) | First API integrations with Anthropic and OpenAI; provider-level structural differences |
| [`day3_prompt_engineering`](./day3_prompt_engineering) | Structured prompting, reliable JSON output, few-shot prompting |
| [`day4_python_patterns`](./day4_python_patterns) | Exception handling, retry logic with exponential backoff, timeout handling |
| [`day5_n8n_automation`](./day5_n8n_automation) | Webhook → LLM automation workflow, and an AI Agent workflow demonstrating autonomous tool selection |

## Key Technical Highlights

**Reliable structured output.** Enforcing JSON schemas in prompts and defensively parsing model output (stripping markdown code fences before `json.loads()`) to build a dependable extraction pipeline — see [`day3_prompt_engineering/structured_prompting.py`](./day3_prompt_engineering/structured_prompting.py).

**Generalization via few-shot prompting.** Two examples of compensation-type normalization were enough for the model to correctly classify an unseen "revenue-share" compensation structure — see [`day3_prompt_engineering/few_shot_prompting.py`](./day3_prompt_engineering/few_shot_prompting.py).

**Resilient API calls.** Differentiated retry logic that distinguishes transient failures (rate limits, connection errors — retried with exponential backoff) from permanent failures (authentication errors — raised immediately) — see [`day4_python_patterns/retry_logic.py`](./day4_python_patterns/retry_logic.py).

**Automation vs. agentic behavior.** Two n8n workflows in [`day5_n8n_automation`](./day5_n8n_automation) illustrate the distinction directly:
- `basic_automation_workflow.json` — a fixed, developer-defined sequence (Webhook → LLM call → Respond)
- `ai_agent_preview_workflow.json` — an AI Agent that autonomously decides whether and when to invoke a Calculator tool based on the input, rather than following a hardcoded path

## Stack

Python · Anthropic API · OpenAI API · n8n · `python-dotenv`

## Author

Sravani Balne — Full Stack Developer / Tech Lead transitioning into AI development.
[LinkedIn](https://www.linkedin.com/in/sravanibalne/) · [GitHub](https://github.com/sravanibalne)
