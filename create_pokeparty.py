import requests
import random
import urllib
from IPython.display import display
from PIL import Image

party_list = []

def search_pokemon(name):
        try: 
            convert = str.lower(name)
            response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{convert}/")
            pokemon = response.json()
            poke_attr = {}
            level = random.randint(1, 100)
            poke_attr["Name"] = pokemon["name"]
            poke_attr["Lvl"] = level
            poke_attr["HP"] = level*3
            moves = pokemon.get("moves", [])
            moves_set = [move["move"]["name"] for move in moves]
            held_items = pokemon.get("held_items", [])
            poke_attr["moves"] = (", ").join(random.sample(moves_set, 4))
            poke_attr["held items"] = (", ").join([item["item"]["name"] for item in held_items])
            poke_attr["sprites"] = pokemon["sprites"]["front_default"]
            party_list.append(poke_attr)
        except: 
            print("Pokemon not yet discovered")

def print_party(var):
        for item in var:
            img_url = item["sprites"]
            urllib.request.urlretrieve(img_url, "1.png")
            img = Image.open("1.png").quantize(colors=10,method=1).convert('RGB').convert('HSV')
            display(img)
            print(
              "=============================" +
              "\nName: " + str.title(item["Name"]) +
              "\nLvl: " + str(item["Lvl"]) +
              "\nHP: " + str(item["HP"]) +
              "\nMoves: " + str(item["moves"]) +
              "\nHeld Items: " + str(item["held items"])
              )
          
if __name__ == "__main__":
    pokemon = input("List the pokemons in your party: ")
    poke_list = pokemon.split()
    for i in poke_list:
        search_pokemon(i)
    print_party(party_list)