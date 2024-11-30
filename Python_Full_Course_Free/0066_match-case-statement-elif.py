# Match-case statement (switch): An alternative to using many "elif" statements
#                                Execute some code if a value matches a "case"
#                                Benefits: cleaner and syntax is more readable

def day_of_week(day):

    if day == 1:
        return "It is Sunday"
    elif day == 2:
        return "It is Monday"
    elif day == 3:
        return "It is Tuesday"
    elif day == 4:
        return "It is Wednesday"
    elif day == 5:
        return "It is Thursday"
    elif day == 6:
        return "It is Friday"
    elif day == 7:
        return "It is Saturday"
    else:
        return "Not a valid day"

print(day_of_week(1))