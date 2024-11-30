# list comprehension = A concise way to create lists in Pytho
#                      Compact and easier to read than traditional loops
#                      [expression for value in iterable if condition]

fruits = ["apple", "orange", "banana", "coconut"]
fruits = [fruit.upper() for fruit in fruits]
print(fruits)