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

# ------------------------------------------------
# Internal Helper: station validation
# -------------------------------------------------
def _is_valid_station(text:str) -> bool:
    """ Filter out non-station noise from Yahoo transit HTML """
    if not text:
        return False
    
    # Obvious noise keywords
    noise_keywords = [
        "ドーナツ", "カフェ", "レストラン", "ショップ", "store", "shop"
    ]

    if any(kw in text for kw in noise_keywords):
        return False

    # must contain Japanese / Kanji characters (basic heuristic)
    return bool(re.search(r"[ぁ-んァ-ン一-龯]", text))

# ----------------------------------------------
# Main Parser
# ----------------------------------------------

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
    # Fare (summary-first, fallback-safe)
    # ---------------------------------------------------------
    fare = "N/A"

    fare_li = route_summary.select_one("li.fare")

    if fare_li:
        text = fare_li.get_text(" ", strip=True)
        match = re.search(r"(\d[\d,]*)円", text)
        if match:
            fare = match.group(0)

    # ---------------------------------------------------------
    # Stations
    # ---------------------------------------------------------
    stations = []
    for station in route_detail.find_all("div", class_="station"):
        dt = station.find("dt")
        if dt:
            name = dt.get_text(strip=True)

            # 🔥 filter noise here
            if _is_valid_station(name):
                stations.append(name)

    transfer_stations = stations[1:-1] if len(stations) > 2 else []

    # ---------------------------------------------------------
    # Train lines
    # ---------------------------------------------------------
    train_lines = []
    for segment in route_detail.find_all("div", class_="fareSection"):
        line_info = segment.select_one("ul li div")
        if not line_info:
            continue

        text = line_info.get_text(strip=True)

        if not text or len(text) <= 2:
            continue

        # detect walking explicitly (no fare implications)
        is_walk = ("徒歩" in text) or ("walk" in text.lower())

        train_lines.append({
            "type": "walk" if is_walk else "train",
            "label": text
        })

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