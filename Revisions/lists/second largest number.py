numbers = [45, 89, 23, 89, 67, 90, 90]

largest = numbers[0]
second_largest = None

for num in numbers:
    if num > largest:
        second_largest = largest #make the old largest second largest
        largest = num #and update the new largest
    elif num != largest and (second_largest is None or num > second_largest): #if num is not largest and second largest is greater than it
        second_largest = num #then update it and make it second largest

print(second_largest)