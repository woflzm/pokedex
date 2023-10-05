class Pokemon:
    def __init__(self, name, hp, attacks, held_items): # def __init__ is used when a new object is created; self is the first argument when using __init__
        self.name = name
        self.hp = hp
        self.attacks = attacks
        self.held_items = held_items

    def __str__(self):
        return f"""
Name: {self.name}
HP: {self.hp}
Attacks: {", ".join(self.attacks)}
Held items: {", ".join(self.held_items)}
"""

def create_pokemon():
    name = input("Enter the Pokémon's name: ").capitalize()
    hp = input("Enter the Pokémon's HP (e.g., 154/154): ")
    attacks = input("Enter the Pokémon's attacks (separated by commas): ").split(",")
    held_items = input("Enter the Pokémon's held items (separated by commas): ").split(",")

    return Pokemon(name, hp, attacks, held_items)

def main():
    pokemons = []

    # Prompt the user to enter data for 6 Pokémons
    for i in range(1):
        pokemon = create_pokemon()
        pokemons.append(pokemon)

    #Show information about all Pokémons
    for pokemon in pokemons:
        print(pokemon)

if __name__ == "__main__": #ensure that your code is only executed when you want it to be executed
    main()