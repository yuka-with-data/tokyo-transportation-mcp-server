""" 
# Transit Fetcher

Responsible for retrieving raw HTML data from the Yahoo Japan Transit search endpoint.
This module handles only network requests (I/O).
No parsing, formatting, or any other logic should live here.
 """

import requests

BASE_URL = "https://transit.yahoo.co.jp/search/print"

def fetch_transit_html(departure: str, arrival: str) -> str | None:
    """
    Fetch raw HTML from Yahoo Transit search.
    MCP design: return raw data only.
    """

    params = {
        "from": departure,
        "to": arrival
    }

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114 Safari/537.36"
        )
    }

    try:
        response = requests.get(BASE_URL, params=params, headers=headers, timeout=10)

        if response.status_code != 200:
            return None

        return response.text

    except requests.RequestException:
        return None