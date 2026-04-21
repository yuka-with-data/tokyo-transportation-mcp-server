""" 
MCP Tool: Get Route
Thin wrapper that exposes the route_service to MCP clients.
Accepts structured input, calls the service layer, and returns
structured JSON output (No formatting or scraping)
 """

from typing import Dict, Any
from tokyo_mcp.services.route_service import get_route

def _split_travel_time(travel_time:str) -> Dict[str,str]:
    """ 
    Helper Function:
    Split 'HH:MM発→HH:MM着' into departure and arrival time.
      """
    try:
        dep, arr = travel_time.split("→")
        departure_time = dep.replace("発", "").strip()
        arrival_time = arr.replace("着", "").strip()

        return {
            "departure_time": departure_time,
            "arrival_time": arrival_time,
        }
    except Exception:
        return {
            "departure_time": None,
            "arrival_time": None,
        }


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

    # If error, pass through
    if "error" in result:
        return result

    # Normalize travel_time → split into structured fields
    if "travel_time" in result:
        time_data = _split_travel_time(result["travel_time"])
        result.update(time_data)
        del result["travel_time"]

    return result

# Export for MCP server registration
__all__ = ["get_route_tool"]