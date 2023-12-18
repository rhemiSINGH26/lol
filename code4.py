import random

class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, enemy):
        damage = random.randint(1, self.power)
        enemy.health -= damage
        print(f"{self.name} attacks {enemy.name} and deals {damage} damage!")

    def is_alive(self):
        return self.health > 0

def battle(player, enemy):
    print(f"A wild {enemy.name} appears!\n")
    while player.is_alive() and enemy.is_alive():
        print(f"{player.name}: {player.health} HP | {enemy.name}: {enemy.health} HP")
        player.attack(enemy)
        if enemy.is_alive():
            enemy.attack(player)
            print("")
    if player.is_alive():
        print(f"{player.name} defeated {enemy.name}!")
    else:
        print(f"{player.name} was defeated by {enemy.name}...")

def main():
    print("Welcome to Battle Arena!")
    player_name = input("Enter your character's name: ")
    player_choice = input("Choose your character (Warrior/Mage/Rogue): ").lower()

    if player_choice == "warrior":
        player = Character(player_name, 100, 15)
    elif player_choice == "mage":
        player = Character(player_name, 80, 20)
    elif player_choice == "rogue":
        player = Character(player_name, 90, 18)
    else:
        print("Invalid choice. Default character (Warrior) selected.")
        player = Character(player_name, 100, 15)

    enemies = [Character("Goblin", 50, 10), Character("Orc", 70, 12), Character("Dragon", 120, 25)]
    random_enemy = random.choice(enemies)

    print("\nLet the battle begin!\n")
    battle(player, random_enemy)

if __name__ == "__main__":
    main()


