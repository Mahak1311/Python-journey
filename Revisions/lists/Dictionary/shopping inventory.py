inventory = {
    "Milk":15,
    "Bread":8,
    "Butter":12,
    "Eggs":30
}
inventory.update({"Milk": 13, "Eggs": 25})
print(inventory)

buy = int(input("Enter quantity of bread: "))

if buy > inventory["Bread"]:
    print("Not enough stock")
else:
    inventory["Bread"] -= buy
    print("Updated inventory:")
    print(inventory)


