import pandas as pd

# Load existing data from a CSV file if it exists, otherwise create an empty DataFrame
try:
    pokemon_data = pd.read_csv('pokemon_data.csv', index_col=0) #index_col=0 to start at index 0
except FileNotFoundError: #create a df
    pokemon_data = pd.DataFrame(columns=['name', 'hp', 'attacks', 'held_items'])

# Function to add a new Pokémon to the DataFrame
def add_pokemon():
    name = input("Enter Pokémon name: ").capitalize()
    hp = input("Enter HP (current/total, e.g., 30/30): ")  #Example input: '30/30'
    attacks = [attack.strip().capitalize() for attack in input("Enter attack/s (comma-separated): ").split(',')]
    held_items = [item.strip().capitalize() for item in input("Enter held items (comma-separated): ").split(',')]

    global pokemon_data
    new_data = pd.DataFrame({'name': [name], 'hp': [hp], 'attacks': [attacks], 'held_items': [held_items]})
    pokemon_data = pd.concat([pokemon_data, new_data], ignore_index=True)

    print("Pokémon added successfully!")


# Function to remove a Pokémon from the DataFrame
def remove_pokemon():
    name = input("Enter Pokémon name to remove: ").capitalize()
    global pokemon_data
    print("Before Removal:")
    print(pokemon_data)  # Print DataFrame before removal
    pokemon_data = pokemon_data[pokemon_data['name'] != name]
    print("After Removal:")
    print(pokemon_data)  # Print DataFrame after removal
    print("Pokémon removed successfully!")


# Function to display Pokémon data in the specified format
def display_pokemon_data():
    print("\nDisplay Options:")
    print("1. Show All Pokémon")
    print("2. Search Pokémon by Name")
    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nAll Pokémon Data:")
        for index, row in pokemon_data.iterrows():
            print(f"Name: {row['name']}")
            print(f"HP: {row['hp']}")
            print(f"Attacks: {', '.join(row['attacks'])}")
            print(f"Held Items: {', '.join(row['held_items'])}")
            print()
    elif choice == "2":
        search_name = input("Enter Pokémon name to search: ")
        found_pokemon = pokemon_data[pokemon_data['name'] == search_name]
        if not found_pokemon.empty:
            print("\nFound Pokémon Data:")
            for index, row in found_pokemon.iterrows():
                print(f"Name: {row['name']}")
                print(f"HP: {row['hp']}")
                print(f"Attacks: {', '.join(row['attacks'])}")
                print(f"Held Items: {', '.join(row['held_items'])}")
                print()
        else:
            print(f"No Pokémon found with the name '{search_name}'.")
    else:
        print("Invalid choice. Please try again.")

# Interactive menu
while True:
    print("\nPokemon Database Menu:")
    print("1. Add Pokemon")
    print("2. Remove Pokemon")
    print("3. Show Pokemon Data")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_pokemon()
    elif choice == "2":
        remove_pokemon()
    elif choice == "3":
        display_pokemon_data()
    elif choice == "4":
        # Save data to CSV before exiting
        pokemon_data.to_csv('pokemon_data.csv', index=False)
        print("Data saved successfully. Exiting.")
        break
    else:
        print("Invalid choice. Please try again.")
