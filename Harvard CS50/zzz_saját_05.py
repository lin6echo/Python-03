x = int(input("What's x?"))


if x % 2 == 0:
    print("This wasn't prime number.")
elif x % 1 == 0 and x % x == 0:
    print("It was prime number")


