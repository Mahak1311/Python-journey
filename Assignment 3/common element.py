#check whether common elements exist in 2 list
list1 = [1, 2, 3, 4]
list2 = [3, 5, 7, 9]

set1 = set(list1)
set2 = set(list2)

common = set1 & set2

if common:
    print("Lists share common elements")
    print("Common elements:", common)
else:
    print("Lists do not share any common elements")