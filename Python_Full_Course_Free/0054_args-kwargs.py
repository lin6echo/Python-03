def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

#    for value in kwargs.values():
#        print(value, end=" ")

    print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')}")
    print(f"{kwargs.get('state')}")
    print(f"{kwargs.get('zip')}")


shipping_label("Dr.", "Spongebob", "Harold", "Squarepants",
                street="123 Fake St.",
                apt="100",
                city="Detroit",
                state="MI",
                zip="54321")