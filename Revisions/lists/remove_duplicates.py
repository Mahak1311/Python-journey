#remove duplicates without using sets
movies = [
    "Inception",
    "Dark",
    "Money Heist",
    "Dark",
    "Inception",
    "Wednesday"
]
duplicate=[]
for movie in movies:
    if movie not in duplicate:
        duplicate.append(movie)

print(duplicate)      

