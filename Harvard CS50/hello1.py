# Ask user for their name
'''name = input("What's your name? ")'''

# Say hello to user
'''print("hello,", name) one way'''

#another way with end
'''print("hello, ", end="")
print(name)'''

#another  way with sep
'''print("hello,", name, sep=" ")'''

#remove whitespace from str
'''name = name.strip()'''

#Capitolize user's name
'''name = name.capitalize()
name = name.title()'''

#remove whitespace from str and capitalize user's name
'''name = name.strip().title()'''

#simpliest way
name = input("What's your name? ").strip().title()

#split user's name into first name and last name
'''first, last = name.split(" ")
print(f"hello, {first}")'''

print(f"hello, {name}")