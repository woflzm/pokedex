import requests 
import sys


def get_pokemon_data(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}/"
    response = requests.get(url)
    pokemon = response.json()

    if response.status_code == 200:
       return pokemon
    else:
        print("There's a problem fetching data")
        return None

def get_pokemon_name(name):
    pokemon_data = get_pokemon_data(name)
    
    if pokemon_data:
        pokemon_name = pokemon_data["name"]
        first_letter = pokemon_name[0].upper()
        return (first_letter + pokemon_name[1:])


def get_pokemon_hp(name):
    pokemon_data = get_pokemon_data(name)
    return pokemon_data["stats"][0]["base_stat"]


def get_pokemon_held_items(name):
    pokemon_data = get_pokemon_data(name)
    held_items = pokemon_data.get("held_items", [])
    return ", ".join(item["item"]["name"] for item in held_items) if held_items else "No Held Items Found"

def get_pokemon_moves(name):
    pokemon_data = get_pokemon_data(name)
    moves = pokemon_data.get("moves", [])
    move_names = [move["move"]["name"] for move in moves]
    return ", ".join(move_names) if move_names else "No Moves Found"

def main():
    if len(sys.argv) > 2:
        print("Please insert a pokemon name")
        return

    pokemon_name = sys.argv[1]
    pokemon_data = get_pokemon_data(pokemon_name)

    if not pokemon_data:
        print(f"Pokemon '{pokemon_name}' not found.")
        return

    print(f"Pokemon Name: {get_pokemon_name(pokemon_name)}")
    print(f"HP: {get_pokemon_hp(pokemon_name)} / {get_pokemon_hp(pokemon_name)} ")
    print(f"Held Items: {get_pokemon_held_items(pokemon_name)}")
    print(f"Moves: {get_pokemon_moves(pokemon_name)}")

if __name__ == "__main__":
    main()