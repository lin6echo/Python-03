import re

email = input("What's your email?").strip()

#if re.search(".+@.+", email):

# fix domain
if re.search(r"^[^@]+@[^@]+\.hu$", email):

    print("Valid")
else:
    print("Invalid")