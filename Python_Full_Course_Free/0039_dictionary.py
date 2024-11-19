# dictonary = a collection of {key:value} pairs
#             ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# print(capitals.get("USA"))
'''
if capitals.get("Japan"):
    print("That capital exist")
else:
    print("That capital doesn't exist")
'''
# capitals.update({"Germany": "Berlin"}) # add a new key-value pair
# capitals.pop("China") # remove key-value pair
# capitals.popitem() # remove the latest key-value pair
# capitals.clear() # empty dictionary
'''
keys = capitals.keys()

for key in capitals.keys():
    print(key)
'''
'''
values = capitals.values()
#print(values)
for value in capitals.values():
    print(value)
''' 

# items = capitals.items()


for key, value in capitals.items():
    print(f"{key}: {value}")




