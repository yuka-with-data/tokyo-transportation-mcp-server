"""
MCP Tool: Get Route
Thin wrapper that exposes the route_service to MCP clients.
Accepts structured input, calls the service layer, and returns
structured JSON output (No formatting or scraping)
 """

from typing import Dict, Any, Optional
from tokyo_mcp.services.route_service import get_route
from tokyo_mcp.utils.query_parser import parse_query
from tokyo_mcp.utils.time_parser import parse_travel_time

# ---------------------------------------------------
# MCP Tool
# ----------------------------------------------------
def get_route_tool(
        departure: Optional[str] = None,
        arrival: Optional[str] = None,
        query: Optional[str] = None
    ) -> Dict[str, Any]:
    """
    MCP-compatible route tool.
    Args:
        departure (str): Starting station (e.g., "Shinjuku")
        arrival (str): Destination station (e.g., "Shibuya")
        query (str)

    Returns:
        dict: Structured route data or error object
    """

    # Step 1: NLP path (if query provided)
    if query:
        parsed = parse_query(query)

        if "error" in parsed:
            return parsed

        departure = parsed.get("departure")
        arrival = parsed.get("arrival")

    # Step 2: Validate
    if not departure or not arrival:
        return {
            "error": "invalid_input",
            "reason": "missing_departure_or_arrival"
        }

    # Step 3: Call service layer
    result = get_route(departure, arrival)

    if "error" in result:
        return result

    # Step 4: Normalize travel time
    if "travel_time" in result:
        result.update(parse_travel_time(result["travel_time"]))
        del result["travel_time"]

    return result

# Export for MCP server registration
__all__ = ["get_route_tool"]
