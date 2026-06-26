# AGENTS.md
## Purpose
This repository contains an MCP project with reusable AI Skills. Follow the repository conventions and prefer existing implementations over introducing new patterns.

## Startup
Before making changes:
1. Read this `AGENTS.md`.
2. If the task relates to the repository's Skill, load its SKILL.md before proceeding.

## SKill Loading
The Skill is located under `.agents/skills/`.

When a task clearly matches the Skill, use the Skill's instructions as the primary source of domain-specific guidance. Avoid duplicating Skill content in this document.

## Validation
When modifying the MCP server or Skill behavior:
- Run relevant tests or evals when available.
- If validation cannot be completed, clearly state what was not verified.

## Safety
- Avoid destructive or irreversible actions at any time.
- Do not modify files
- Ask for clarification if the requested change is ambiguous.