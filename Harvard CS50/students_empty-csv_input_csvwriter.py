import csv

name = input("What's your name?")
home = input("Where's your home?")

with open("empty.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])