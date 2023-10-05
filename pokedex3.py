class Pokemon:
    def __init__(self, name, hp, attacks, held_items):
        self.name = name
        self.hp = hp
        self.attacks = attacks
        self.held_items = held_items

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"HP: {self.hp}")
        print(f"Attacks: {', '.join(self.attacks)}")
        print(f"Held Items: {', '.join(self.held_items)}")

def main():
    pokemon_list = []

    for _ in range(6):
        name = input("Enter Pokémon name: ")
        hp = input("Enter HP (e.g., 154/154): ")
        attacks = input("Enter attacks (comma-separated, e.g., scratch,flamethrower): ").split(',')
        held_items = input("Enter held items (comma-separated, e.g., king's stone,nanab berry): ").split(',')

        pokemon = Pokemon(name.strip(), hp.strip(), [attack.strip() for attack in attacks], [item.strip() for item in held_items])
        pokemon_list.append(pokemon)

    print("\nPokémon Information:")
    for pokemon in pokemon_list:
        pokemon.display_info()


if __name__ == "__main__":
    main()
