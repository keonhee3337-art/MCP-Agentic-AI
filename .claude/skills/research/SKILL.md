---
name: research
description: Use when asked to research a topic, find recent information, or do deep investigation on something. Calls the Perplexity API (sonar model) with live web search and saves a full report to the research/ folder. Use this (not the research sub-agent) when quality matters more than cost.
---

# Skill: Research

Deep, context-aware research using Perplexity's sonar model with live web search. Goes beyond a quick web search — synthesizes multiple queries, filters for relevance to Keonhee's context, and saves a full report.

## Trigger phrases
- "research X"
- "do deep research on X"
- "investigate X"
- "find out everything about X"
- "I need a research report on X"
- "look into X for me"

## What Claude does

1. **Load context** — read `context/me.md`, `context/work.md`, `context/current-priorities.md`, `context/goals.md`
2. **Understand the question** — frame it in relation to Keonhee's goals, priorities, and active projects
3. **Formulate 2-3 targeted queries** — specific enough to get useful results, not generic
4. **Read `.env`** — get `PERPLEXITY_API_KEY`
5. **Call Perplexity API** via Bash for each query:

```bash
curl -s "https://api.perplexity.ai/chat/completions" \
  -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "sonar",
    "messages": [{"role": "user", "content": "YOUR_QUERY_HERE"}]
  }'
```

6. **Synthesize results** — combine findings, prioritize what's relevant to Keonhee's context, include sources
7. **Save full report** to `research/YYYY-MM-DD-[topic-slug].md` — include all sources, full detail
8. **Present summary in chat** — bullets only, key findings, link to saved report

## Output format (in chat)

- 3-5 bullet points, most relevant findings first
- Flag anything directly tied to current priorities
- One line: "Full report saved to research/[filename].md"

## Notes

- Always load context first — research should be tailored, not generic
- Save the report even for quick requests — it builds the knowledge base over time
- For quick, shallow lookups — use the `web-search` skill instead
- To keep costs low and delegate to a cheaper model — use the `research-agent` sub-agent instead
