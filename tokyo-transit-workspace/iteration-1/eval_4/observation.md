# Eval 4 Analysis: Skill vs Without Skill

## Summary

Eval 4 tested whether the `tokyo-transit` Skill improves agent behavior for a realistic transit planning request.

Task:

> I am visiting Tokyo for the first time. What is the best way to get from Shinjuku Station to Tokyo DisneySea?

## Observation

Both With Skill and Without Skill versions:

- Correctly used Tokyo Transit MCP tools.
- Returned valid transit routes.
- Provided complete route information including transfers, travel time, and fares.
- Did not fall back to web search.

However, the selected routes were different.

### With Skill

- Route: Shinjuku → Ichigaya → Shin-Kiba → Maihama → Tokyo DisneySea
- Fare: 816 yen
- Travel time: ~72 minutes
- More transfer points

### Without Skill

- Route: Shinjuku → Tokyo → Maihama → Tokyo DisneySea
- Fare: 740 yen
- Travel time: ~69 minutes
- Fewer transfers

The Without Skill version selected a simpler and more commonly recommended route for a first-time visitor.

## Analysis

The Skill successfully influenced tool usage by keeping the agent within the Tokyo Transit MCP workflow.

However, this evaluation did not show that the Skill improved route decision quality. In this case, the Skill-enabled output selected a valid but less optimal route with higher fare and additional transfers.

This suggests that adding a Skill layer does not automatically improve agent decisions after tool selection.

Future evaluations should test whether the Skill can consistently guide the agent toward better route preferences when multiple valid routes exist.

Expected behavior:

> When multiple valid routes exist, prefer routes with fewer transfers and lower fare when travel times are comparable.
