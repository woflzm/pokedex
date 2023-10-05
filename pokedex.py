import requests
import sys

def search_pokemon(name):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")
    #response = requests.get("https://pokeapi.co/api/v2/pokemon/charmander")
    pokemon = response.json()
    print("Name: " + str(pokemon["name"].capitalize()))
    print("ID: " + str(pokemon["id"]))
    print("Base XP: " + str(pokemon["base_experience"]))

if __name__ == "__main__":
    search_pokemon(sys.argv[1])