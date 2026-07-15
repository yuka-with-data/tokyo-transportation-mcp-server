"""
Utility functions for parsing transit-related time information.

This module provides helper functions used across Tokyo MCP services
and tools to convert raw transit time strings into structured data.

The parsed output is used by route planning and MCP tool layers to
provide consistent departure and arrival time fields.

Functions:
    parse_travel_time(travel_time):
        Parse a transit time string into departure and arrival times.

Output:
    {
        "departure_time": "10:00",
        "arrival_time": "10:45"
    }

If parsing fails, the function returns None values for the time fields.
"""

def parse_travel_time(travel_time: str) -> dict:
    """
    Parse travel time string into departure and arrival times.

    Args:
        travel_time (str): Travel time information, e.g.
            "10:00発 → 10:45着"

    Returns:
        dict: Parsed departure and arrival times.
    """
    try:
        dep, arr = travel_time.split("→")

        return {
            "departure_time": dep.replace("発", "").strip(),
            "arrival_time": arr.replace("着", "").strip(),
        }

    except Exception:
        return {
            "departure_time": None,
            "arrival_time": None,
        }
