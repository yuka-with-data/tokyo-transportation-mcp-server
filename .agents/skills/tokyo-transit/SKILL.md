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