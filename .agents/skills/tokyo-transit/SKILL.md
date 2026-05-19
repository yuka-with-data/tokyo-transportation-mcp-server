---
name: tokyo-transit
description: >
  Tokyo rail transit and route planning skill for station-to-station
  navigation across the greater Tokyo metropolitan rail network,
  including subway, JR, private railway, and connected transit systems.
  Use this skill for route planning, transfer guidance, travel time
  estimation, and Tokyo transportation assistance.
license: Apache-2.0
compatibility: >
  Designed for Codex and Agent Skills-compatible runtimes. Requires
  access to the Tokyo Transit MCP tools and related route planning
  services.
metadata:
  domain: transportation
  region: Tokyo, Japan
  version: 0.1.1
allowed-tools: route_tool arrival_planner_tool
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

This skill focuses on transportation workflow and routing assistance, not geenral tourism planning or booking operations.

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
- Use commonly recognized station names in responses

## Output Rules
Responses should:
- present stations in travel order
- identify operators and line names
- clearly indicate transfers
- provide estimated travel duration when available
- remain concise and readable

Preferred response structure:
1. Route summary
2. Transfer sequence
3. Estimated travel time
4. Additional notes (if needed)