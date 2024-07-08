import sys

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = 'village'

    def __str__(self):
        return f'{self.name}, Health: {self.health}, Inventory: {self.inventory}, Location: {self.location}'

def intro():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a small village with a path leading into a dark forest.")
    print("Your goal is to find the hidden treasure in the forest.")
    
def character_creation():
    name = input("Enter your character's name: ")
    return Player(name)

def village(player):
    print("\nYou are in the village.")
    print("1. Go to the forest")
    print("2. Check your inventory")
    choice = input("What do you want to do? ")
    if choice == '1':
        forest(player)
    elif choice == '2':
        check_inventory(player)
        village(player)
    else:
        print("Invalid choice.")
        village(player)

def forest(player):
    print("\nYou enter the dark forest.")
    print("1. Explore deeper")
    print("2. Go back to the village")
    choice = input("What do you want to do? ")
    if choice == '1':
        encounter(player)
    elif choice == '2':
        player.location = 'village'
        village(player)
    else:
        print("Invalid choice.")
        forest(player)

def encounter(player):
    print("\nYou encounter a wild beast!")
    print("1. Fight")
    print("2. Run")
    choice = input("What do you want to do? ")
    if choice == '1':
        fight(player)
    elif choice == '2':
        run(player)
    else:
        print("Invalid choice.")
        encounter(player)

def fight(player):
    print("\nYou chose to fight the beast.")
    if "sword" in player.inventory:
        print("With your sword, you defeat the beast!")
        player.inventory.append("beast fang")
        print("You found a beast fang and added it to your inventory.")
    else:
        print("You have no weapon. The beast injures you.")
        player.health -= 20
    player.location = 'forest'
    forest(player)

def run(player):
    print("\nYou run back to the village.")
    player.location = 'village'
    village(player)

def check_inventory(player):
    print(f"\nYour inventory: {player.inventory}")

def main():
    intro()
    player = character_creation()
    village(player)

if __name__ == "__main__":
    main()
