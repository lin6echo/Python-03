name = input("Enter your full name: ")

# result = name.find("a") # 2 (caracter index) first occurrence
result = name.rfind("a") # 4 last occurrence

print(result)