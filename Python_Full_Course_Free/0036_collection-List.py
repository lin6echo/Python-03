# collection = single "variable" used to store multiple velues
#    List    = [] ordered and changeable, Duplicates OK.
#     Set    = {} unordered and immutable, but Add/Remove OK. No duplicates.
#   Tuple    = () ordered and unchangeable. Duplicates OK. Faster.

fruits = ["apple", "orange", "banana", "coconut" ]

# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("apple" in fruits)
# fruits[0] = "pineapple"
# fruits.append("pineapple")
# print(fruits[1]) # [] index operator
# for fruit in fruits:
# fruits.remove("apple")
# fruits.insert(0, "pineapple")
# fruits.sort()
# fruits.reverse()
# fruits.clear()
# print(fruits.index("apple"))
print(fruits.count("banana"))

print(fruits)