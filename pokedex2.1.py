import requests
import sys

def search_pokemon(name):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")
    #response = requests.get("https://pokeapi.co/api/v2/pokemon/charmander")
    pokemon = response.json()

def __str__(name):
    return f"""
    Name: pokemon["name"].capitalize()
    ID: pokemon["id"]
    Base XP: pokemon["base_experience"]
 """

if __name__ == "__main__":
    search_pokemon(sys.argv[1])