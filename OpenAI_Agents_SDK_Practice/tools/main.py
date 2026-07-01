from agents import function_tool 
import requests
@function_tool
async def weather_tool(city:str):
    """
    A tool to get the current weather for a given city.
    """
    response = requests.get(f"https://wttr.in/{city}?format=j1")
    return response.json()