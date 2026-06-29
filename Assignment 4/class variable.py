class Player:

    player_count = 0      # Class Variable

    def __init__(self, name, level):
        self.name = name      # Instance Variable
        self.level = level    # Instance Variable

        Player.player_count += 1

    def display(self):
        print("Name:", self.name)
        print("Level:", self.level)


# User Input

n = int(input("How many players? "))

players = []

for i in range(n):
    name = input("Enter player name: ")
    level = int(input("Enter player level: "))

    p = Player(name, level)
    players.append(p)

print("\nPlayer Details:")

for p in players:
    p.display()
    print()

print("Total Players Created:", Player.player_count)