# Skill: Database Builder

Scaffold databases for projects — in Notion (via MCP) or as local structured files.

## Trigger phrases
- "create a database for X"
- "set up a project tracker for X"
- "build a Notion database for X"
- "scaffold a data structure for X"

## How to use
Describe what you need to track. Examples:
- "Create a Notion database to track my AI projects"
- "Build a database for logging decisions across all my projects"
- "Set up a tracker for my AI CPA exam study sessions"
- "Scaffold a local JSON/CSV structure for storing web search results"

## What Claude does
1. Asks clarifying questions if the use case is unclear (what are you tracking, what fields matter)
2. Designs the schema — fields, types, relationships
3. Creates it via Notion MCP if connected, or outputs a local file structure
4. Adds a README or usage note so you know how to maintain it

## Output format
- Schema summary as a table (field name, type, purpose)
- Creation confirmation or local file path
- One-line note on how to update/maintain it

## Notes
- For Notion: requires Notion MCP to be active in Claude Code
- For local: defaults to a markdown table or JSON depending on use case
- Say "make it simple" for a minimal version, "make it comprehensive" for full structure
