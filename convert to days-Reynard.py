def convert_to_days():
    days = (hours / 24) + (minutes / 60 / 24) + (seconds / 60 / 60 / 24)
    return days


hours = int(input("Enter a number of hours: "))
minutes = int(input("Enter a number of minutes: "))
seconds = int(input("Enter a number of seconds: "))
print("The number of day is: ", convert_to_days())
