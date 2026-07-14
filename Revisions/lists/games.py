#Favorite game
games = ["Minecraft", "Valorant", "GTA", "PUBG", "Chess"]
for game in games[:3]: #includes 0,1,2
    print("First 3 games: ",game)

for game in games[3:]: #includes 3 and 4
    print("Last 2 games: ", game)   

for game in games[::-1]: #reverses a list using slicing start:end:step
    print(game)    