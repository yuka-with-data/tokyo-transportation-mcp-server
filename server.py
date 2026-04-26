""" 
MCP Server Entry Point

Registers MCP tools and exposes them to clients.
This is the bridge between external clients and internal logic.
 """

from mcp.server.fastmcp import FastMCP
from tokyo_mcp.tools.route_tool import get_route_tool
from tokyo_mcp.tools.arrival_planner_tool import get_arrival_planning_tool

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

@mcp.tool()
def plan_arrival(
    origin: str,
    destination: str,
    target_arrival_time: str,
    buffer_minutes: int = 10
):
    """ 
     Plan departure time based on desired arrival time
      Args:
         origin (str): Starting station
        destination (str): Destination station
        target_arrival_time (str): Desired arrival time "HH:MM"
        buffer_minutes (int): Safety buffer time. MUST be >= 10. Default is 10.

      Returns:
         dict: Recommended departure + route info
       """
    # -----------------------------------------------------
    # MCP boundary enforcement (safe defaults for LLM calls)
    # -----------------------------------------------------
    if buffer_minutes is None or buffer_minutes <= 0:
        buffer_minutes = 10
    else:
        buffer_minutes = int(buffer_minutes)

    # ---------------------------------------------
    # Delegate to MCP tool wrapper 
    # ---------------------------------------------
    return get_arrival_planning_tool(
        origin=origin,
        destination=destination,
        target_arrival_time=target_arrival_time,
        buffer_minutes=buffer_minutes
    )

# ----------------------------------------
# Run Server
# ----------------------------------------
if __name__ == "__main__":
    mcp.run()