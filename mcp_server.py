from mcp.server.fastmcp import FastMCP
import requests

mcp = FastMCP("my_mcp_server", stateless_http=True, port=8087)


@mcp.tool()
async def magic_number():
    return 27


@mcp.tool()
async def get_random_joke():
    """Fetch a random joke from the Official Joke API."""
    resp = requests.get("https://official-joke-api.appspot.com/random_joke")
    resp.raise_for_status()
    return resp.json()


@mcp.tool()
async def get_random_advice():
    """Fetch a random piece of advice from the Advice Slip API."""
    resp = requests.get("https://api.adviceslip.com/advice")
    resp.raise_for_status()
    return resp.json()


@mcp.tool()
async def get_random_cat_fact():
    """Fetch a random cat fact from the Cat Fact API."""
    resp = requests.get("https://catfact.ninja/fact")
    resp.raise_for_status()
    return resp.json()


@mcp.tool()
async def get_random_user():
    """
    Fetch a random user from the Random User API and extract relevant fields from a complex JSON.
    """
    resp = requests.get("https://randomuser.me/api/")
    resp.raise_for_status()
    return resp.json()


@mcp.tool()
async def get_weather_forecast(latitude: float = 35, longitude: float = 139):
    """
    Fetch weather forecast from Open-Meteo API (complex JSON).
    """
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m,precipitation",
    }
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    return resp.json()


@mcp.tool()
async def get_random_meal():
    """
    Fetch a random meal from TheMealDB API and extract relevant fields.
    """
    resp = requests.get("https://www.themealdb.com/api/json/v1/1/random.php")
    resp.raise_for_status()
    return resp.json()


@mcp.tool()
async def get_pokemon_info(pokemon_name: str = "pikachu"):
    """
    Fetch information about Pikachu from the PokéAPI (complex JSON).
    """
    resp = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
    resp.raise_for_status()
    return resp.json()


@mcp.tool()
async def get_country_info(country: str = "japan"):
    """
    Fetch country information from the REST Countries API.
    """
    resp = requests.get(f"https://restcountries.com/v3.1/name/{country}")
    resp.raise_for_status()
    return resp.json()


@mcp.tool()
async def get_random_dog_image():
    """
    Fetch a random dog image from Dog CEO's Dog API.
    """
    resp = requests.get("https://dog.ceo/api/breeds/image/random")
    resp.raise_for_status()
    return resp.json()


@mcp.tool()
async def get_universities_by_country(country: str = "United States"):
    """
    Fetch a list of universities in a given country from the Universities API.
    """
    resp = requests.get(f"http://universities.hipolabs.com/search?country={country}")
    resp.raise_for_status()
    return resp.json()


def main():
    mcp.run(transport="streamable-http")


if __name__ == "__main__":
    main()
