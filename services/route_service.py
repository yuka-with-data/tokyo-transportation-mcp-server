""" 
# Route Service (Orchestrator)

Coordinate the transit pipeline:
1. Fetch raw HTML (transit_fetcher)
2. Parse route data(transit_parser)
3. Apply station normalization (data/stations)

This layer contains No scrapig, No parsing logic, and No MCP/tool interface code. 
 """
from services.transit_fetcher import fetch_transit_html
from services.transit_parser import parse_transit_html
from data.stations import get_japanese_station_name

def get_route(departure: str, arrival: str) -> dict:
    """
    Main MCP-ready route service.

    Args:
        departure (str): Starting station (English or raw input)
        arrival (str): Destination station (English or raw input)

    Returns:
        dict: Structured route information or error object
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
    # Fetch HTML
    # -----------------------------
    html = fetch_transit_html(departure_jp, arrival_jp)

    if not html:
        return{
            "error": "fetch_failed",
            "departure": departure_jp,
            "arrival": arrival_jp,
        }
    
    # ------------------------------
    # Parse route data
    # ------------------------------
    route_data = parse_transit_html(html)

    if not route_data:
        return {
            "error": "parse_failed",
            "departure": departure_jp,
            "arrival": arrival_jp,
        }
    
    # ---------------------------------
    # Attach normalized metadata
    # ---------------------------------
    route_data["departure"] = departure_jp
    route_data["arrival"] = arrival_jp

    return route_data