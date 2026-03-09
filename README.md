# MCP Agentic AI — Second Brain & AI Tooling System

An agentic AI second brain built on Claude Code (VS Code), Model Context Protocol (MCP), and a custom skills/agents architecture. This repository is the operational core — context files, skills, sub-agents, hooks, and automation that make Claude progressively smarter across sessions.

---

## Architecture

```
CLAUDE.md               ← Master brain file. Loads all context via @ imports.
context/                ← Persistent facts: identity, work, priorities, goals
.claude/
  skills/               ← 9 domain skills (triggered by phrase or slash command)
  agents/               ← 5 specialist sub-agents (model-assigned, fresh context)
  settings.json         ← Hooks: rm -rf guard, automated safety checks
decisions/log.md        ← Append-only architectural decision log
references/sops/        ← Standard operating procedures
```

---

## Skills (9 active)

| Skill | Purpose |
|-------|---------|
| `research` | Deep web research via Perplexity API (sonar model). Saves full report to `research/`. |
| `financial-analyst` | Adapted from Anthropic's Cowork finance plugin. Korean market, DART data, income statement analysis, investment thesis. |
| `data-analyst` | Pandas, SQLite, NumPy, OpenAI embeddings, Streamlit visualization. |
| `geo` | Generative Engine Optimization — structures public content for AI citation (GitHub, LinkedIn, READMEs). |
| `web-search` | Quick lookups via live web search. |
| `interview-prep` | Structures prep for AI/consulting role interviews. Research, talking points, mock Q&A. |
| `code-researcher` | Finds and evaluates code approaches for agentic AI projects. |
| `database-builder` | Scaffolds Notion or local project databases. |
| `chat-log-summarizer` | Pulls and summarizes past conversation context across sessions. |

---

## Agents (5 specialist sub-agents)

| Agent | Model | Role |
|-------|-------|------|
| `director-agent` | Sonnet | Orchestrator. Decomposes goals, delegates to specialists, synthesizes results. |
| `coding-agent` | Sonnet | AI project development. LangGraph, RAG, FastAPI, Streamlit, custom VectorDB. |
| `writing-agent` | Haiku | External documents. Cover letters, applications, business plans. |
| `notion-agent` | Haiku | Notion MCP operations. Create pages, search, log decisions. |
| `research-agent` | Haiku | Cheap/fast research via Perplexity API. |

---

## Automation

- **Pre-commit hook** — blocks `.env`, `.env.local`, `.env.production`, `secrets.toml` from being committed
- **PreToolUse hook** — warns before any Bash command containing `rm -rf`
- **Cron (Monday 9am KST)** — auto-generates weekly focus plan to `templates/weekly-focus.md`

---

## MCP Integrations

- **Notion** — connected. Used for project tracking, decision logging, research storage.
- **n8n** — planned. Setup guide: `projects/n8n-integration/README.md`

---

## Context

Built by **Keonhee**, Business Administration student at Sungkyunkwan University (SKKU), South Korea.
Active projects: [FinAgent](https://keonhee-finagent.streamlit.app) — multi-agent financial analysis system (LangGraph + RAG + Text2SQL, deployed).

**Stack in use:** Claude Code, MCP (Model Context Protocol), LangGraph, RAG, custom VectorDB, Python, Perplexity API, OpenAI API, Notion API.
