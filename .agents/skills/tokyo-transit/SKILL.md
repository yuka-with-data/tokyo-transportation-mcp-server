---
name: tokyo-transit
description: Helps plan routes across Tokyo's rail network with travel times, transfers, and fares.
license: Apache-2.0
compatibility: Requires git, docker, jq, and access to the internet
metadata:
  author: yuka-with-data
  domain: transportation
  region: Tokyo, Japan
  version: "1.0"
---
# Tokyo Transit MCP Server

## Overview

Tokyo Transit MCP Server provides rail transit routing and transportation assistance across the greater Tokyo metropolitan railway network.

The skill is designed for:

- station-to-station route planning
- transfer guidance
- travel time estimation
- rail operator navigation
- transit-oriented travel assistance

Supported systems include:

- JR Lines
- Tokyo Metro
- Toei Subway
- private railways
- connected regional rail system

This skill focuses on transportation workflow and routing assistance, not general tourism planning or booking operations. When this skill is active, the MCP transit service MUST be initialized and used for all route generation. Web search must not be used as a substitute.

## Activation Criteria

Activate this skill when the user:

- asks how to travel between stations
- references Tokyo train stations or rail operators
- requests the fastest, simplest, or cheapest route
- asks about train transfers
- requests arrival or departure timing support

Example triggers:

- "How do I get from Shinjuku to Asakusa?"
- "Best route from Tokyo Station to Yokohama?"
- "Which line goes to Shibuya?"
- "How many transfers to Maihama?"

## Tool Usage

### `route_tool`

Use for:

- station-to-station routing
- transfer discovery
- line navigation
- route comparison

Expected inputs:

- origin station
- destination station
- optional route constraints

### `arrival_planner_tool`

User for:

- arrival estimation
- departure timing support
- schedule-aware planning
- time-sensitive routing

Expected inputs:

- route information
- target arrival or departure timing

## Routing Rules

- Prefer lower-transfer routes when travel times are similar
- Prefer faster express routes for long-distance travel
- Clearly identify transfer stations and operators
- Clarify ambiguous station names before routing
- if origin or destination is missing, request clarification before generating a route
- Use commonly recognized station names in responses

## Fare Calculation Rules

- Always use route summary fare as the primary source of truth when available
- Do not compute total fare from individual segments
- Walking segments are informational only and must not contribute to fare
- Segment-level parsing is allowed only for explanation, not pricing

## Output Rules

Responses should:

- present stations in travel order
- identify operators and line names
- clearly indicate transfers
- provide estimated travel duration when available
- include total fare for completed route results whenever fare data exists
- remain concise and readable

Preferred response structure:

1. Route summary
2. Transfer sequence
3. Estimated travel time
4. Total fare
5. Additional notes (if needed)

## Failure Handling

If routing fails:

- request clarification for ambiguous station names
- confirm spelling when needed
- explain unavailable route information clearly
- provide best-effort guidance when partial data exists

If tool results conflict:

- prioritize the most complete route result

## Progressive Disclosure

Load external references only when explicitly needed based on user intent or routing context.

- `references/operator_rules.md`→ when routing involves operator-specific behavior, transfers, or through-services

## Examples

### Simple Route

User:
> How do I get from Shinjuku to Ueno?

Behavior:

- use `route_tool`
- generate optimal route
- present transfer guidance and estimated travel time

### Transfer Route

User:
> Best route from Tokyo station to Maihama?

Behavior:

- compute transfer-aware route
- identify transfer requirements
- present travel duration and transfer sequence

### Ambiguous Query

User:
> Route to Shinagawa

Behavior:

- clarify missing origin station
- request additional routing context
