# Iteration 1

This iteration evaluates how the 'tokyo-transit' Skill affects agent behavior when working with the Tokyo Transit MCP tools.

## Evaluation Progression

| Eval | Scenario | Primary Focus |
| --- | --- | --- |
| 1 | Tokyo Station → Shinjuku Station | Basic MCP route extraction |
| 2 | Shinjuku Station → Tokyo DisneySea | Attraction/station resolution and transit details |
| 3 | Shinjuku Station → Tokyo Tower | Landmark resolution |
| 4 | Natural-language DisneySea request | Skill influence on route selection |
| 5 | Shinjuku Station → Toyosu Station with transfer preference | Skill routing rules |
| 6 | Arrive at Tokyo Station by a specific time | Skill-driven MCP tool selection |

## Key Finding So Far

Evals 1-3 produces essentially identical results with and without the Skill.

Eval 4 showed a more meaningful differences: both versions used the MCP tools and produced valid routes, but the Skill-enabled version selected a route with a higher fare and more transfers.

Eval 5 showed a different result: the Skill-enabled version selected a route with fewer transfers, lower fare, and shorter travel time, better matching the user's explicit preference.

This suggests that a Skill does not automatically improve agent decisions; its impact depends both on the underlying tools and on how the Skill is defined to guide the agent.

## Evaluation Results

| Eval | Query Type | With Skill vs Without Skill | Current Finding |
| --- | --- | --- | --- |
| 1 | Simple station-to-station route | Nearly identical | Little measurable Skill impact |
| 2 | Station → attraction route | Very similar | MCP already handles the task well |
| 3 | Station → landmark route | Identical | Little measurable Skill impact |
| 4 | Natural-language, more complex route request | Different routes | Skill changed behavior, but selected a less optimal route |
| 5 | Route request with explicit transfer preference | Different routes | Skill better aligned the route with the user's preference |
| 6 | Time-sensitive route planning | Identical | MCP handled the task well; Skill had no measurable impact |

## Current Hypothesis

The more complex or preference-driven the user query becomes, the more opportunity the Skill has to influence agent behavior.
