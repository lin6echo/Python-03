# format specifiers = {value:flags} format a value based on what
#                              flags are insserted


price1 = 3.14159
price2 = -987.65
price3 = 12.34

# .(number)f = round to that many decimal places (fixed point)
print(f"Price 1 is ${price1:.2f}") # Price 1 is $3.14
print(f"Price 2 is ${price2:.2f}") # Price 2 is $-987.65
print(f"Price 3 is ${price3:.2f}") # Price 3 is $12.34

# :(number) = allocate that many spaces
print(f"Price 1 is ${price1:10}") # Price 1 is $   3.14159
print(f"Price 2 is ${price2:10}") # Price 2 is $   -987.65
print(f"Price 3 is ${price3:10}") # Price 3 is $     12.34


# :03 = allocate and zero pad that many spaces
print(f"Price 1 is ${price1:010}") # Price 1 is $0003.14159
print(f"Price 2 is ${price2:010}") # Price 2 is $-000987.65
print(f"Price 3 is ${price3:010}") # Price 3 is $0000012.34

# :< = left justify
print(f"Price 1 is ${price1:<10}") # Price 1 is $3.14159
print(f"Price 2 is ${price2:<10}") # Price 2 is $-987.65
print(f"Price 3 is ${price3:<10}") # Price 3 is $12.34 


# :> = right justify
print(f"Price 1 is ${price1:>10}") # Price 1 is $   3.14159
print(f"Price 2 is ${price2:>10}") # Price 2 is $   -987.65
print(f"Price 3 is ${price3:>10}") # Price 3 is $     12.34

# :^ = center align
print(f"Price 1 is ${price1:^10}") # Price 1 is $ 3.14159 
print(f"Price 2 is ${price2:^10}") # Price 2 is $ -987.65
print(f"Price 3 is ${price3:^10}") # Price 3 is $  12.34 

# :+ = use a plus sign to indicate positiv value
print(f"Price 1 is ${price1:+}") # Price 1 is $+3.14159
print(f"Price 2 is ${price2:+}") # Price 2 is $-987.65
print(f"Price 3 is ${price3:+}") # Price 3 is $+12.34

# := = place sign to leftmost position
print(f"Price 1 is ${price1:=}") # Price 1 is $3.14159
print(f"Price 2 is ${price2:=}") # Price 2 is $-987.65
print(f"Price 3 is ${price3:=}") # Price 3 is $12.34

# :  = insert a space before positive numbers
print(f"Price 1 is ${price1: }") # Price 1 is $ 3.14159
print(f"Price 2 is ${price2: }") # Price 2 is $-987.65
print(f"Price 3 is ${price3: }") # Price 3 is $ 12.34

price1 = 3000.14159
price2 = -9870.65
price3 = 1200.34

# :, = comma separator
print(f"Price 1 is ${price1:,}") # Price 1 is $3,000.14159
print(f"Price 2 is ${price2:,}") # Price 2 is $-9,870.65
print(f"Price 3 is ${price3:,}") # Price 3 is $1,200.34








