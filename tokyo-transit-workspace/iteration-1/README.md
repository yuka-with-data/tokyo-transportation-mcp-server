# Iteration 1

This iteration evaluates how the 'tokyo-transit' Skill affects agent behavior when working with the Tokyo Transit MCP tools.

## Evaluation Progression

| Eval | Scenario | Primary Focus |
| --- | --- | --- |
| 1 | Tokyo Station → Shinjuku Station | Basic MCP route extraction |
| 2 | Shinjuku Station → Tokyo DisneySea | Attraction/station resolution and transit details |
| 3 | Shinjuku Station → Tokyo Tower | Landmark resolution |
| 4 | Natural-language DisneySea request | Skill influence on route selection |
| 5 | Shinjuku Station → Tokyo Station with transfer preference | Skill routing rules |
| 6 | Arrive at Tokyo Station by a specific time | Skill-driven MCP tool selection |


## Key Finding So Far

Evals 1-3 produces essentially identical results with and without the Skill.

Eval 4 showed a more meaningful differences: both versions used the MCP tools and produced valid routes, but the Skill-enabled version selected a route with a higher fare and more transfers.

This suggests that a Skill does not automatically improve agent decisions; its impact depends both on the underlying tools and on how the Skill is defined to guide the agent.

Eval 5 and 6 will investigate whether the Skill can influence:

- route preference decisions
- selection of the appropriate MCP tool
