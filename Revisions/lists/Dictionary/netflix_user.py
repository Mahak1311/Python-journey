#Netflix user
user = {
    "name": "Rahul",
    "subscription": "Premium",
    "watch_time": 120
}
for value in user.values():
    print(value) #to only print value

user["subscription"]="Basic" #to change to basic
print(user)
user["watch_time"]+=30 #to increase watch time by 30
print(user)
user.update({"city":"Ahmedabad"}) #to add another key and value
print(user)
value= user.pop("watch_time") #to delete watch time
print(user)