""" Unit tests for the route_service module. """
# ------------------------------------------------------
# Mock service layer
# ------------------------------------------------------
# pylint: disable=too-few-public-methods
class MockTransitService:
    """ Mock transit service used for route service tests. """
    def get_route(self, departure, arrival):
        """ Return a predictable mock route response. """
        return {
            "departure": departure,
            "arrival": arrival,
            "travel_time": "45分 発 10:00 着 10:45",
            "fare": "300円",
            "stations": ["A", "B", "C"],
            "transfers": ["B"],
            "train_lines": ["JR Yamanote Line"]
        }

def mock_get_transit_service():
    """Return a mock transit service instance."""
    return MockTransitService()

def identity(value):
    """Mock station name lookup by returning the input unchanged."""
    return value

def test_get_route_success(monkeypatch):
    """ Verify that the route service returns the expected route data. """
    # pylint: disable=import-outside-toplevel
    from tokyo_mcp.services import route_service
    # --------------------------------------------------
    # Patch dependencies
    # --------------------------------------------------
    monkeypatch.setattr(
        route_service,
        "get_transit_service",
        mock_get_transit_service
    )

    monkeypatch.setattr(
        route_service,
        "get_japanese_station_name",
        identity
    )

    # --------------------------------------------------
    # Run
    # --------------------------------------------------
    result = route_service.get_route("Shinjuku", "Shibuya")

    # --------------------------------------------------
    # Assertions
    # --------------------------------------------------
    assert "発" in result["travel_time"]
    assert "着" in result["travel_time"]
    assert "円" in result["fare"]
    assert "stations" in result
