# *args    = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments
#            * unpacking operator
#            1. positional 2. default 3. keyword 4. ARBITRARY

# def add(a, b):
#     return a + b

# print(add(1, 2))

def add(*args):
    total = 0 
    for arg in args:
        total += arg
    return total
    
    
print(add(1, 2, 3))