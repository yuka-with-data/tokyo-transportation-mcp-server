from services.route_service import get_route

# ------------------------------------------------------
# Mock dependencies
# ------------------------------------------------------
class MockFetcher:
    @staticmethod
    def fetch_transit_html(departure, arrival):
        return "<html>mock html</html>"


def mock_parser(html):
    return {
        "travel_time": "45 min",
        "fare": "300円",
        "stations": ["A", "B", "C"],
        "transfers": ["B"],
        "train_lines": ["JR Yamanote Line"]
    }


def test_get_route_success(monkeypatch):
    """
    Test full route service flow (success case)
    """

    from services import route_service

    # --------------------------------------------------
    # Patch dependencies
    # --------------------------------------------------
    monkeypatch.setattr(
        route_service,
        "fetch_transit_html",
        lambda dep, arr: "<html>mock</html>"
    )

    monkeypatch.setattr(
        route_service,
        "parse_transit_html",
        mock_parser
    )

    monkeypatch.setattr(
        route_service,
        "get_japanese_station_name",
        lambda x: x  # bypass normalization
    )

    # --------------------------------------------------------
    # Run
    # --------------------------------------------------------
    result = route_service.get_route("Shinjuku", "Shibuya")

    # ----------------------------------------------
    # Assertions
    # -----------------------------------------------
    assert result["travel_time"] == "45 min"
    assert result["fare"] == "300円"
    assert "stations" in result