# Skill: Chat Log Summarizer

Summarize past conversation context so you don't have to dig through old chat logs manually.

## Trigger phrases
- "summarize this conversation"
- "what did we cover so far"
- "catch me up"
- "what decisions did we make today"
- "summarize [topic] from our earlier discussion"

## How to use
- At any point in a session: "summarize what we've covered so far"
- End of session: "give me a session summary" — Claude fills out `templates/session-summary.md`
- Cross-session: paste in a previous chat log and say "summarize this"

## What Claude does
1. Reads the conversation (current session or pasted log)
2. Extracts: what got done, decisions made, open items, anything to remember
3. Returns a structured summary in the format below

## Output format
**What Got Done**
- [bullet list]

**Decisions Made**
- [bullet list]

**Open Items / Next Steps**
- [bullet list]

**Anything to Log**
- Decisions worth adding to `decisions/log.md`
- Preferences to remember

## Notes
- At end of session, say "close out this session" and Claude will write the summary directly to `templates/session-summary.md` with today's date
- If a decision came up that matters long-term, Claude will prompt you to log it in `decisions/log.md`
