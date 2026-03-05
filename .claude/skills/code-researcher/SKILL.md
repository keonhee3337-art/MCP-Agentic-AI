# Skill: Code Researcher

Find, evaluate, and explain code approaches for agentic AI projects — without you having to hunt through docs or Stack Overflow manually.

## Trigger phrases
- "find code for X"
- "what's the best way to build X"
- "how do I implement X in [tool/framework]"
- "compare approaches for X"
- "show me an example of X using LangChain / Claude API / etc."

## How to use
Be specific about what you're building. Examples:
- "Find code for building a multi-step agent using LangChain"
- "What's the best way to connect Claude to a Notion database via MCP"
- "Show me how to stream responses with the Claude API"
- "Compare LangChain vs raw Claude API for an agentic workflow"

## What Claude does
1. Searches for relevant implementations (docs, repos, examples)
2. Returns a clean, working code snippet with explanation
3. Flags tradeoffs if multiple approaches exist
4. Notes which tools/versions it applies to

## Output format
- One-line explanation of what the code does
- Code block (clean, minimal, no fluff)
- Bullet points on key things to know (gotchas, dependencies, version notes)
- If comparing approaches: short table of tradeoffs

## Notes
- Always specify the framework or tool if you have a preference
- Say "explain this like I need to present it" if you want an explanation suitable for an interview or pitch
- For full project scaffolds, say "scaffold a project that does X" instead
