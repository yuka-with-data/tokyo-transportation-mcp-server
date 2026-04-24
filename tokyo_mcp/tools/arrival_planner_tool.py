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
     dict: Recommended departure plan + route info
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