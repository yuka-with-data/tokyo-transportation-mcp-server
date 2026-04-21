""" 
MCP Server Entry Point

Registers MCP tools and exposes them to clients.
This is the bridge between external clients and internal logic.
 """

from mcp.server.fastmcp import FastMCP
from tokyo_mcp.tools.route_tool import get_route_tool

# Initialize MCP server
mcp = FastMCP("tokyo-transport-server")

# ------------------------------------------
# Tool Registration
# ------------------------------------------
@mcp.tool()
def get_route(departure:str, arrival:str):
    """ 
     Get train route between two stations.
     Args:
        departure(str): Starting station
        arrival(str): Destination station

     Returns:
        dict: Route information (time, fare, stations, etc.)
       """
    return get_route_tool(departure, arrival)

# ----------------------------------------
# Run Server
# ----------------------------------------
if __name__ == "__main__":
    mcp.run()