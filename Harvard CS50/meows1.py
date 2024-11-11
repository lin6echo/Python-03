def meow(n: int) -> str:
    return "meow\n" * n


    '''for _ in range(n):
        print("meow")'''

number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")