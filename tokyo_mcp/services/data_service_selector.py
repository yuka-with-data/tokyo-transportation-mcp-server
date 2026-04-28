from config import USE_EXPERIMENTAL

def get_transit_service():
    if USE_EXPERIMENTAL:
        from tokyo_mcp.services.experimental.temp_fetcher import fetch_transit_html
        from tokyo_mcp.services.experimental.temp_parser import parse_transit_html

        class ExperimentalService:
            def get_route(self, departure_jp, arrival_jp):
                html = fetch_transit_html(departure_jp, arrival_jp)
                if not html:
                    return None

                return parse_transit_html(html)

        return ExperimentalService()

    else:
        # placeholder for now
        pass