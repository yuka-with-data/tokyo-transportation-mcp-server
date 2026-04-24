""" 
Service: Planning Service

Computes recommended departture time based on a target arrival time
using route duration from route_service.
 """
from typing import Dict, Any, Optional
from datetime import datetime, timedelta
from tokyo_mcp.services.route_service import get_route

# -----------------------------------------------
# Internal Helper Function
# -----------------------------------------------
def _parse_hhmm(time_str: str) -> Optional[datetime]:
    """ Parse "HH:MM" into a datetime object (today's date)"""
    try:
        return datetime.strptime(time_str, "%H:%M")
    except Exception:
        return None

def _travel_time_to_minutes(dep_time: str, arr_time:str) -> Optional[int]:
    """ 
     Convert departure and arrival time into duration in minutes.
     Assumes same day (no overnight handling just yet)
       """
    try:
        dep = _parse_hhmm(dep_time)
        arr = _parse_hhmm(arr_time)

        if not dep or not arr:
            return None # invalid time format
        
        # Compute time difference
        delta = arr - dep
        # Convert to minutes
        return int(delta.total_seconds() // 60)
    except Exception:
        return None # fallback on failure

def _split_travel_time(travel_time:str) -> Dict[str,str]:
    """ 
    Helper Function:
    Split 'HH:MM発→HH:MM着' into departure and arrival time.
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
    
# -------------------------------------------
# Main Service
# -------------------------------------------
def get_departure_for_arrival(
        origin:str,
        destination: str,
        target_arrival_time: str,
        buffer_minutes: int = 10
) -> Dict[str, Any]:
    """ 
     Compute recommended departure time to meet a target arrival.

    Args:
        origin (str): Starting station
        destination (str): Destination station
        target_arrival_time (str): "HH:MM"
        buffer_minutes (int): Optional safety buffer

    Returns:
        dict: Planning result with route + recommended departure
     """
    # Step 1: Get route data
    route = get_route(origin, destination)

    if "error" in route:
        return route

    # Step 2: Extract travel time from route
    travel_time = route.get("travel_time")

    if not travel_time:
        return {
            "error": "invalid_route_data",
            "reason": "missing_travel_time"
        }

    # Step 3: Split travel time into departure/arrival
    time_data = _split_travel_time(travel_time)

    dep_time = time_data.get("departure_time")
    arr_time = time_data.get("arrival_time")

    if not dep_time or not arr_time:
        return {
            "error": "time_parse_failed",
            "reason": "could_not_split_travel_time"
        }

    # Step 4: Compute travel duration
    travel_minutes = _travel_time_to_minutes(dep_time, arr_time)

    if travel_minutes is None:
        return {
            "error": "time_parse_failed",
            "reason": "could_not_compute_travel_duration"
        }

    # Step 5: Parse target arrival time
    target_dt = _parse_hhmm(target_arrival_time)

    if not target_dt:
        return {
            "error": "invalid_input",
            "reason": "invalid_target_arrival_format"
        }
    
    # Step 6: Compute recommended departure
    # Subtract travel + buffer from target arrival
    recommended_dt = target_dt - timedelta(minutes=travel_minutes + buffer_minutes)
    # Format as HH:MM string
    recommended_departure = recommended_dt.strftime("%H:%M")

    # Step 6: Return structured result
    return {
        "origin": route.get("departure"),
        "destination": route.get("arrival"),
        "target_arrival_time": target_arrival_time,
        "recommended_departure_time": recommended_departure,
        "estimated_travel_time_minutes": travel_minutes,
        "buffer_minutes": buffer_minutes,
        "route": route
    }