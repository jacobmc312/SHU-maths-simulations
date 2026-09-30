year = input("Enter a year: ")
year = int(year)
if year % 400 == 0:
    print("Leap year!!!")
elif year % 4 == 0 and year % 100 != 0:
    print("Leap year!!!")
else:
    print("not a leap year :(")
