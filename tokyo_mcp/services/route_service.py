""" 
# Route Service (Orchestrator)

Coordinate the transit pipeline:
1. Fetch raw HTML (transit_fetcher)
2. Parse route data(transit_parser)
3. Apply station normalization (data/stations)

This layer contains No scrapig, No parsing logic, and No MCP/tool interface code. 
 """
from tokyo_mcp.services.data_service_selector import get_transit_service
from tokyo_mcp.data.stations import get_japanese_station_name

def get_route(departure: str, arrival: str) -> dict:
    """
    This function acts as the main interface between MCP tools and the transit backend system.

    Args:
        departure (str): Starting station (English or raw input)
        arrival (str): Destination station (English or raw input)

    Returns:
        {
            "departure": str,
            "arrival": str,
            "travel_time": str,
            "fare": str,
            ... (backend-dependent fields)
        }
    """
    # ------------------------------
    # Normalize station names
    # ------------------------------
    departure_jp = get_japanese_station_name(departure)
    arrival_jp = get_japanese_station_name(arrival)

    if not departure_jp or not arrival_jp:
        return{
            "error": "invalid_station_name",
            "departure": departure,
            "arrival": arrival,
        }
    
    # -----------------------------
    # Select backend data service [Experimental]
    # -----------------------------
    service = get_transit_service()

    # Delegate route fetching to select backend
    route_data = service.get_route(departure_jp, arrival_jp)

    # Handle failure from backend service
    if not route_data:
        return {
            "error": "route_not_found",
            "departure": departure_jp,
            "arrival": arrival_jp,
        }

    # ---------------------------------
    # Attach normalized metadata
    # ---------------------------------
    route_data["departure"] = departure_jp
    route_data["arrival"] = arrival_jp

    return route_data