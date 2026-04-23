""" 
Query Parser Utility

Convers natural language user queries into structured 
departure/arrival station inputs for MCP tools.

Purpose: 
This query parser exists to translate messy human language into clean, 
structured inputs so MCP tools stay deterministic and resuable.

Uses:
- spaCy for entity extraction (primary)
- regex patterns as fallback (robustness)

Output is always a structured dict.
 """

from typing import Dict, Optional
import re
import spacy

from tokyo_mcp.data.stations import get_japanese_station_name
nlp = spacy.load("en_core_web_sm")

# ---------------------------------------------
# Internal Helpers
# ----------------------------------------------
def _extract_with_spacy(text: str):
    """ Extract station candidiates using spaCy NER """
    doc = nlp(text)

    # Look for location-like entities
    locations = [ent.text for ent in doc.ents if ent.label_ in ("GPE", "LOC")]

    if len(locations) >= 2:
        return locations[0], locations[1]

    return None, None

def _extract_with_regex(text: str):
    """Fallback extraction using common patterns."""
    patterns = [
        r"from\s+(.*?)\s+to\s+(.*)",
        r"to\s+(.*?)\s+from\s+(.*)",
        r"(.*?)\s*→\s*(.*)",
        r"(.*?)\s*-\s*(.*)",
        r"(.*?)\s+to\s+(.*)",
    ]

    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            departure = match.group(1).strip()
            arrival = match.group(2).strip()
            return departure, arrival

    return None, None

def _clean_station(text: str) -> str:
    """
    Lightweight cleanup for extracted station names.
    Keeps names intact but removes noise from NLP/regex.
    """

    if not text:
        return None

    # Trim whitespace
    text = text.strip()

    # Remove trailing punctuation noise
    text = re.sub(r"[?？.!！,，]+$", "", text)

    return text

# ---------------------------------------------
# Public API
# ----------------------------------------------
def parse_query(user_query: str) -> Dict[str, Optional[str]]:
    """ 
     Parse user query into structured departure and arrival.
     Args:
        user_query(str): Natural language input

     Returns:
        dict: {
            "departure": str | None,
            "arrival": str | None,
            "error": optional
        }
       """
    # NLP extraction
    departure, arrival = _extract_with_spacy(user_query)

    # Fallback to regex if needed
    if not departure or not arrival:
        departure, arrival = _extract_with_regex(user_query)

    # Cleanup step
    departure = _clean_station(departure)
    arrival = _clean_station(arrival)
    
    # Validate
    if not departure or not arrival:
        return {
            "departure": None,
            "arrival": None,
            "error": "parse_failed",
            "reason": "could_not_extract_stations"
        }

    # Normalize (English -> Japanese station names)
    departure_jp = get_japanese_station_name(departure)
    arrival_jp = get_japanese_station_name(arrival)

    if not departure_jp or not arrival_jp:
        return {
            "departure": None,
            "arrival": None,
            "error": "invalid_station",
            "reason": "station_not_found"
        }
    
    return {
        "departure": departure_jp,
        "arrival": arrival_jp
    }