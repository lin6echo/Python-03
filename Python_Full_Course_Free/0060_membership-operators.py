# Membership operators = used to test whether a value or variable is found in a sequence
#                        (string, list, tuple, set or dictionary)
#                        1. in
#                        2. not in

students = {"Spongebob", "Patrick", "Sandy"}

student = input("Enter the name of a student: ")

if student in students:
    print(f"{student} is a student")
else:
    print(f"{student} was not found")