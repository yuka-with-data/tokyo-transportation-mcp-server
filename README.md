# 🚆Tokyo MCP Server
![License](https://img.shields.io/badge/license-Apache%202.0-blue)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Status](https://img.shields.io/badge/status-demo--project-orange)
![Architecture](https://img.shields.io/badge/design-MCP%20architecture-purple)
![Use Case](https://img.shields.io/badge/use--case-AI%20Agents-green)
## Overview
Tokyo MCP Server is a modular backend designed to provide structured public transportation intelligence for AI agents.

Instead of returning raw or unstructured text, this system exposes transportation capabilities as tools that can be called by an agent. These tools handle route search and arrival-time planning, returning clean, predictable outputs that agents can reliably use in downstream reasoning.

This repository is intended for:
- Developers building AI agents that require transportation knowledge
- Engineers exploring MCP-based architectures
- Contributors interested in modular, tool-driven system design

### Motivation

Tokyo has one of the most complex and heavily used public transportation systems in the world. Despite this, most AI systems today still provide only generic routing suggestions rather than accurate, real-time-aware guidance.

In practice, accessing reliable transit information often requires parsing dedicated services such as Yahoo Transit or other transportation platforms. Without this layer, AI responses tend to lack specificity, timing accuracy, and practical usefulness.

This project was built to bridge that gap.

By structuring transportation logic as callable tools, this MCP server enables AI agents to move beyond vague answers and provide more concrete, context-aware routing support.

At the same time, this project aims to make Tokyo transit more accessible for travelers and non-native residents—allowing them to interact with complex transportation systems using natural language, without needing to navigate multiple unfamiliar local services.

## ⚠️ Project Status & Data Source Note

This repository is a **demonstration of MCP (Model Context Protocol) architecture applied to a real-world transportation use case**.

The current system successfully retrieves and processes real-time transit data, and serves as a working prototype of how MCP tools can be structured and integrated into an agent-based workflow.

However, the current implementation relies on a third-party web-based data source, which was intentionally used during the early development phase to:

* validate MCP tool design
* test end-to-end agent interaction
* iterate quickly on system architecture

### 🔄 Ongoing Transition

To ensure long-term reliability, scalability, and proper data usage, the project is currently being refactored to migrate toward **official, open-source and structured data sources**, such as:

* Open Data Platform for Public Transportation (ODPT)
* GTFS / GTFS-Realtime feeds
* other publicly available or licensed transit APIs

This transition focuses on improving:

* data stability
* system reliability
* architectural integrity

### 🎯 Project Intent

This repository is **not intended as a production-ready transit service**. It is a working prototype designed to explore and validate MCP-based system architecture for transportation use cases.

The project serves as a technical showcase of:

- tool abstraction patterns
- service layer design
- multi-source data integration strategies

The system is currently in an **intermediate stage between rapid prototyping and a more robust, production-oriented architecture**, with ongoing migration toward stable and structured transit data sources.

Contributions are welcome as the project evolves. See **CONTRIBUTING.md** for guidance on how to get involved.


## What is MCP?
**MCP (Model Context Protocol)** is a design pattern for structuring how AI models interact with external tools and systems.

Instead of relying purely on natural language responses, MCP enables models to:
- Call specific tools when needed
- Receive structured outputs
- Chain multiple tool calls as part of reasoning

MCP is based on a **client–server architecture**, where the model acts as the client that issues tool requests, and the server provides tools, data access, and execution logic in a structured and controlled way.

In this project, MCP is implemented by:
- Defining tools (`tools/`) as the interface exposed to the model
- Delegating logic to services (`services/`)
- Returning structured, predictable outputs instead of free-form text

This separation allows the model to focus on decision-making, while the system handles execution and data processing.


## Features
- Route search between stations
- Arrival-time-based route planning
- Clean separation between tools and services
- Structured outputs designed for AI agent consumption
- Modular architecture for easy extension


## Project Structure
```bash
project_root
│   .gitignore
│   pyproject.toml
│   README.md
│   requirements.txt
│   server.py
│
├── tests
│   └── test_route_service.py
│
└── tokyo_mcp
    │   __init__.py
    │
    ├── data
    │   │   stations.py
    │   │   __init__.py
    │
    ├── services
    │   │   planning_service.py
    │   │   route_service.py
    │   │   transit_fetcher.py
    │   │   transit_parser.py
    │   │   __init__.py
    │
    ├── tools
    │   │   arrival_planner_tool.py
    │   │   route_tool.py
    │   │   __init__.py
    │
    └── utils
        │   query_parser.py
        └──   __init__.py
```

## How It Works
The system follows a layered architecture designed for clarity and extensibility:

1. A user (or AI agent) issues a query  
2. The appropriate tool is selected (`tools/`)  
3. The tool calls into a service (`services/`)  
4. The service coordinates:
   - Data fetching (`transit_fetcher`)
   - Data parsing (`transit_parser`)
   - Business logic (e.g., route selection, arrival planning)
5. A structured response is returned to the tool  
6. The tool returns a clean output to the agent  

This design enforces strong separation of concerns:
- Tools define *what* is exposed
- Services define *how* it works
- Utilities support parsing and normalization

As a result, the system remains flexible, testable, and easy to expand with additional transportation capabilities.

## Installation
### 1. Fork the repository
Click the "Fork" button on GitHub to create your own copy.

### 2. Clone your fork
```bash
git clone https://github.com/YOUR-USERNAME/tokyo-transportation-mcp-server.git
cd tokyo-transportation-mcp-server
```

Install dependencies:
```bash
pip install -r requirements.txt
```
## Quick Start (Codex Desktop / Local MCP Client)
Get the MCP server running locally and connect it to a client like Codex Desktop in just a few steps. 
1. Verify the MCP Server (Optional)
You can manually start the server to ensure it runs without errors:
```bash
python server.py
```
2. Connect to the Local MCP Client
This configulation registers your local MCP server and instructs the MCP client to launch it using `python server.py` so the agent can access its tools. 

Configulation Example:
```json
{
  "mcpServers": {
    "tokyo-transport": {
      "command": "python",
      "args": ["server.py"]
    }
  }
}
```
Save the config and restart the local MCP client so it detects the new MCP server.

## Usage
### Example Queries
These are examples of how an AI agent (or MCP client) might interact with the system:

Route Search
- "Find a route from Shibuya to Shinjuku"
- "How do I get from Ueno to Tokyo Station?"

Arrival Planning
- "I want to arrive at Haneda International Airport by 12:00 PM. When should I leave Shibuya?"
- "Plan my trip to Shinjuku from Odaiba, so I arrive before 9 AM"

### Using Tools Programmatically
You can also call the tools directly in Python:
```bash
from tokyo_mcp.tools.route_tool import get_route_tool
from tokyo_mcp.tools.arrival_planner_tool import plan_arrival_tool

route = get_route(origin="Shibuya", destination="Shinjuku")

plan = plan_arrival_tool(
    origin="Shibuya",
    destination="Haneda Airport",
    arrival_time="12:00"
)
```
These functions return structured data that can be used in your own applications or agent workflows. 

## Available Tools
### `get_route`
Finds a transportation route between two stations.

Input:
- `origin`: Starting station
- `destination`: Destination station

Output:
- Departure and arrival times
- Travel duration
- Transfer stations
- Fare information

### `plan_arrival`
Plans a route based on a desired arrival time.

Input:
- `origin`: Starting station
- `destination`: Destination station
- `arrival_time`: Desired arrival time

Output:
- Recommended departure time
- Suggested route
- Travel duration
- Supporting route details

## Running Tests
Run unit tets with:
```bash
pytest
```
### Customizing Tests
This project uses `pytest` for its simplicity and flexibility.
Developers can easily extend the test setup by:
- Adding new test files under tests/
- Using fixtures for reusable test setup
- Parametrizing test cases for broader coverage
- Mocking external calls (e.g., transit fetching)

## Roadmap
The primary focus of this project is currently the migration from experimental scraping-based data sources to stable, structured transit data systems (ODPT / GTFS / related APIs). This migration is foundational to all future improvements.

Planned and potential improvements:
- Data Source Migration (Priority):
    - Replace experimental web scraping with structured transit APIs (ODPT, GTFS)
    - Build a unified transit data abstraction layer
    - Standardize route, station, and timetable data models
    - Improve reliability and consistency of real-time vs static data handling
    - Gradually deprecate experimental adapters
- Adding tools:
    - Fare optimization
    - Multi-route comparison
    - Delay/disruption information
- Smarter planning:
    - Context-aware routing (time of day, rush hour, etc)
    - Multi-step itinerary support
- Multi-agent integration:
    - Coordination between transportation + local recommendation agents
- Developer experience:
    - Better logging and debugging
    - Type hints and validation improvements
- Client layer:
    - Streamlit, Gradio, or web-based interface
    - Visualization (maps, route diagrams)

## Contributing
Please open an issue first, then create a pull request linked to that issue. For the full contribution workflow, please refer to the documentation in [this repository](https://github.com/yuka-with-data/one-commit-a-day/blob/master/resources/contribution-workflow.md).

### Guidelines

* Keep `server.py` stable unless necessary
* Focus changes in `services/` and `tools/`
* Prefer modular and replaceable components
* Avoid introducing new scraping-based dependencies