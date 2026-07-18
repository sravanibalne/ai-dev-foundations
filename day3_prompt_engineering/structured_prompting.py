import os
import json
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

system_prompt = """You are a job posting analyzer. 
Do not wrap the JSON in markdown code fences or backticks. Return raw JSON only.
Extract information and respond ONLY with valid JSON matching this exact schema, no other text:
{
  "role_title": "string",
  "compensation_type": "string (e.g. hourly, salary, revenue-share)",
  "required_skills": ["array", "of", "strings"],
  "is_long_term": true or false
}"""

job_posting = """[Hey! I'm Israel — I run an AI consulting biz called Novus and I'm looking for a developer to come build with me long term. Not a one-off project and NO AGENCIES. I want someone who actually loves this stuff and wants to be part of something growing. A little background on me: 110k+ following, scaled my last business to $50k/month. I know how to sell and grow. What I need is someone who can build. Agents, automations, agentic workflows — the full stack. What we build: Custom AI agents, agentic workflows, and automation systems for business clients. Multi-step agents, LLM pipelines, tool integrations, end-to-end deployments. Who I'm looking for: - You genuinely love building — like side projects at 2am type love - Strong with agentic frameworks (LangChain, CrewAI, n8n, Make, or similar) - Can take a brief and execute without constant hand-holding - Communicates well - In it for the long game — I want someone who grows with us Pay is revenue share — 10 to 30% per client depending on scope. Realistically $5k–$50k pm depending on client volume. No ceiling.]"""

response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=300,
    temperature=0,
    system=system_prompt,
    messages=[{"role": "user", "content": job_posting}]
)

raw_output = response.content[0].text

# Strip markdown code fences if present
cleaned = raw_output.strip()
if cleaned.startswith("```"):
    cleaned = cleaned.split("```")[1]  # grabs content between first pair of fences
    cleaned = cleaned.removeprefix("json").strip()  # remove language tag if present

parsed = json.loads(cleaned)
print(parsed["role_title"])
print(parsed["required_skills"])