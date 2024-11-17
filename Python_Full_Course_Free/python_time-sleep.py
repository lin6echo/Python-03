import time

my_time = int(input("Enter the time in seconds: "))

# for x in reversed(range(1, my_time)):
for x in range(my_time, 0, -1): # another way reverse 
    print(x)
    time.sleep(1)

print("TIME'S UP!")