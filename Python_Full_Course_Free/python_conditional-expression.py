# conditional expression = A one-line schortcut for the if-else statement (ternary operator)
#                          Print or assign one of two values based on a condition
#                          x if condition else Y

num = 5
a = 6
b = 7
age = 25
temperature = 30
user_role = "admin"

# print("Positive" if num > 0 else "Negative")

# result = "Even" if num % 2 == 0 else "Odd"

# max_num =  a if a > b else b
# min_num = a if a < b else b

# print(max_num)
# print(min_num)

# status = "Adult" if age > 18 else "Young"

# print(status)

# weather = "Hot" if temperature > 20 else "Cold"

# print(weather)

access_level = "full access" if user_role == "admin" else "limited access"

print(access_level)