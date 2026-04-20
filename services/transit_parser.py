""" 
# Transit Parser

Responsible for extracting structured route information
from Yahoo japan transit HTML reponses.

Args:
    html (str): Raw HTML string from transit_fetcher
Returns:
    dict | None: Structured route information or None if parsing fails
 """
import re
from bs4 import BeautifulSoup


def parse_transit_html(html: str) -> dict | None:
    """
    Parse Yahoo Transit HTML and extract the top route.
    Returns structured route data.
    """

    soup = BeautifulSoup(html, "html.parser")

    srline = soup.find("div", id="srline")
    if not srline:
        return None

    route_summary = srline.select_one(".routeSummary")
    route_detail = srline.select_one(".routeDetail")

    if not route_summary or not route_detail:
        return None

    # ---------------------------------------------------------
    # Travel time
    # ---------------------------------------------------------
    travel_time_tag = route_summary.select_one("li.time span")
    travel_time = travel_time_tag.get_text(strip=True) if travel_time_tag else "N/A"

    # ---------------------------------------------------------
    # Fare
    # ---------------------------------------------------------
    fare = "N/A"
    fare_li = route_summary.select_one("ul li.fare")

    if fare_li:
        full_text = fare_li.get_text(strip=True)
        match = re.search(r"(\d[\d,]*)円", full_text)
        if match:
            fare = match.group(0)

    # ---------------------------------------------------------
    # Stations
    # ---------------------------------------------------------
    stations = []
    for station in route_detail.find_all("div", class_="station"):
        dt = station.find("dt")
        if dt:
            stations.append(dt.get_text(strip=True))

    transfer_stations = stations[1:-1] if len(stations) > 2 else []

    # ---------------------------------------------------------
    # Train lines
    # ---------------------------------------------------------
    train_lines = []
    for segment in route_detail.find_all("div", class_="fareSection"):
        line_info = segment.select_one("ul li div")
        if line_info:
            train_lines.append(line_info.get_text(strip=True))

    # ---------------------------------------------------------
    # Structured output (MCP-friendly)
    # ---------------------------------------------------------
    return {
        "travel_time": travel_time,
        "fare": fare,
        "stations": stations,
        "transfers": transfer_stations,
        "train_lines": train_lines,
    }