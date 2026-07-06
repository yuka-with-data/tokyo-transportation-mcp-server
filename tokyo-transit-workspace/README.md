# Tokyo Transit Skill Evaluation Workspace
This directory contains evaluation runs for the `tokyo-transit` Agent Skill.

The purpose of these evaluation is to measure how the Skill affects agent behavior  when working with the Tokyo Transit MCP tools.

## Structure
```text
tokyo-transit-workspace/
├── iteration-1/
│   ├── eval-1/
│   │   ├── with_skill/outputs/
│   │   └── without_skill/outputs/
│   └── eval-2/
│       ├── with_skill/outputs/
│       └── without_skill/outputs/
```
- `with_skill/` — Evaluation runs using the `tokyo-transit` Skill.
- `without_skill/` — Baseline runs using MCP tools without the Skill.

## Evaluation Goal
Compare agent outputs with and without the Skill to understand whether the Skill improves:
- MCP tool usage
- Fare accuracy
- Handling of edge cases
- Response consistency

## Notes
Evaluation cases are based on realistic Tokyo transit requests and known areas where agent behavior can be improved.

New iterations should be created when there are significant changes to the Skill, MCP behavior, or evaluation methodology.