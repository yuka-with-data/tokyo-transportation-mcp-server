from tokyo_mcp.services.route_service import get_route

# ------------------------------------------------------
# Mock service layer
# ------------------------------------------------------
class MockTransitService:
    def get_route(self, departure, arrival):
        return {
            "departure": departure,
            "arrival": arrival,
            "travel_time": "45分 発 10:00 着 10:45",
            "fare": "300円",
            "stations": ["A", "B", "C"],
            "transfers": ["B"],
            "train_lines": ["JR Yamanote Line"]
        }


def test_get_route_success(monkeypatch):
    from tokyo_mcp.services import route_service
    # --------------------------------------------------
    # Patch dependencies
    # --------------------------------------------------
    monkeypatch.setattr(
        route_service,
        "get_transit_service",
        lambda: MockTransitService()
    )

    monkeypatch.setattr(
        route_service,
        "get_japanese_station_name",
        lambda x: x
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