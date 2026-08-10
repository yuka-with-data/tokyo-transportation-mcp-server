# Eval 5 Analysis: Skill vs. Without Skill

## Summary

Eval 5 tested whether the `tokyo-transit` Skill influences route selection **when the user explicitly prefers fewer transfers.**

Task:

> I'm traveling with luggage. What's the best way to get from Shinjuku Station to Toyosu Station? Please minimize the number of transfers, even if the route takes a little longer.

## Observation

Both With Skill and Without Skill versions:

- Correctly used the Tokyo Transit MCP tools.
- Returned a valid route.
- Provided travel time, transfers, and fare.

However, the selected routes were significantly different.

### With Skill

- Route: Shinjuku → Ichigaya → Toyosu
- Fare: 317 yen
- Travel time: 26 minutes
- Transfers: 1

### Without Skill

- Route: Shinjuku → Kanda → Yurakucho → Toyosu
- Fare: 431 yen
- Travel time: 37 minutes
- Transfers: 2

The With Skill version selected the route with fewer transfers, lower fare, and shorter travel time, matching the user's explicit preference.

## Analysis

Unlike Eval 4, this evaluation shows a positive effect from the Skill.

The Skill includes the routing rule:

> Prefer lower-transfer routes when travel times are similar.

The Skill-enabled agent selected a one-transfer route, while the Without Skill version selected a two-transfer route that was also slower and more expensive.

This suggests that the Skill can positively influence route selection when its routing guidance aligns with the user's request.

However, the result also reinforces the finding from Eval 4: the impact of a Skill depends on how it is defined and how its guidance interacts with the MCP tool results.

The route was correct, but **the line information in the response was incomplete**; the second segment should identify the Tokyo Metro Yurakucho Line.
