n=int(input("Enter a number: "))

d = 0
for i in range(1, n + 1):
    if (n % i) == 0:
        d += 1
        print(i)


