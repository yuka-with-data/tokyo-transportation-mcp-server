""" 
MCP Tool: Arrival Planner Tool

Wrapper around planning_service that converts a target arrival time
into a recommended departure time.
 """
from typing import Dict, Any
from tokyo_mcp.services.planning_service import get_departure_for_arrival

def get_arrival_planning_tool(
    origin: str,
    destination: str,
    target_arrival_time: str,
    buffer_minutes: int = 10
) -> Dict[str, Any]:
    """ 
     MCP compatible tool for arrival-based route planning.

     Args:
        origin (str): Starting station
        destination (str): Destination station
        target_arrival_time (str): Desired arrival time "HH:MM"
        buffer_minutes (int): Safety buffer time

     Returns:
        dict: {
            "origin": str,
            "destination": str,
            "recommended_departure_time": str,
            "estimated_travel_time_minutes": int,
            "travel_time": str,
            "stations": list[str],
            "transfers": list[str],
            "train_lines": list[str],
            "fare": str
        }
     IMPORTANT:
        Always include route details (stations, transfers, train lines, fare)
        when presenting results to the user.
       """
    if buffer_minutes is None or buffer_minutes <= 0:
        buffer_minutes = 10
    else:
        buffer_minutes = int(buffer_minutes)

    # Direct pass-through to service layer
    return get_departure_for_arrival(
        origin=origin,
        destination=destination,
        target_arrival_time=target_arrival_time,
        buffer_minutes=buffer_minutes
    )

# MCP export
__all__ = ["get_arrival_planning_tool"]