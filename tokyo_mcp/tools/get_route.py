""" 
MCP Tool: Get Route
Thin wrapper that exposes the route_service to MCP clients.
Accepts structured input, calls the service layer, and returns
structured JSON output (No formatting or scraping)
 """

from typing import Dict, Any
from tokyo_mcp.services.route_service import get_route

def get_route_tool(departure: str, arrival: str) -> Dict[str, Any]:
    """
    MCP-compatible route tool.
    Args:
        departure (str): Starting station (e.g., "Shinjuku")
        arrival (str): Destination station (e.g., "Shibuya")

    Returns:
        dict: Structured route data or error object
    """

    # Basic validation
    if not departure or not arrival:
        return {
            "error": "invalid_input",
            "reason": "departure_and_arrival_required"
        }

    # Call service layer
    result = get_route(departure, arrival)

    return result

# Export for MCP server registration
__all__ = ["get_route_tool"]