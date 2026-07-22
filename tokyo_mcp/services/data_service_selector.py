"""
Service selector for choosing the active transit backend.

Currently supports the experiemental HTML parser and
provides a placeholder for future production implementations.
 """
from config import USE_EXPERIMENTAL

def get_transit_service():
    """Returns the active transit service based on the configuration."""
    # Lazy imports are intentional to avoid loading the experimental backend unless configured.
    # pylint: disable=import-outside-toplevel
    if USE_EXPERIMENTAL:
        from tokyo_mcp.services.experimental.temp_fetcher import fetch_transit_html
        from tokyo_mcp.services.experimental.temp_parser import parse_transit_html
    # pylint: enable=import-outside-toplevel

        # pylint: disable=too-few-public-methods
        class ExperimentalService:
            """Experimental transit service implementation."""
            def get_route(self, departure_jp, arrival_jp):
                """ Fetch and parse route information."""
                html = fetch_transit_html(departure_jp, arrival_jp)
                if not html:
                    return None

                return parse_transit_html(html)

        return ExperimentalService()

    # Placeholder for future implementation
    return None
