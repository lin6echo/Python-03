# nested loop = A loop within another loop (outer, inner)
#               outer loop:
#                   inner loop:
# while x > 0:
#   while y > 0:
#       print("do something")

# for x in range(3):
#   for y in range(9):
#       print("do something")

# while x > 0:
#   for y in range(9):
#       print("do something")

# for x in range(3):
#   while y > 0:
#       print("do something")

for x in range(3):
    for y in range(1, 10):
        print(y, end=" ")
    print()


