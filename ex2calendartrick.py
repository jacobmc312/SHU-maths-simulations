print("Please think of a date")
day = int(input("Please enter the day of the month (1, 2, 3, etc.): "))
month = int(input("Please enter the month (1=Jan, 2=Feb, etc.): "))
fullyear = input("Please enter the year (2025, etc.): ")
century = int(fullyear[0:2])
year = int(fullyear[2:])

if (century == 17 and year == 52 and month == 9 and day <= 2) or (century == 17 and year == 52 and month < 9) or (century == 17 and year < 52) or century < 17:
    C = 18 - century
else:
    C = (3 - (century % 4)) * 2

Y = year % 12 + int(year / 12) + int((year % 12) / 4)

month_numbers = []

thismonth = 0
for n in range(1,13):
    month_numbers.append(thismonth)

    if n in (1,3,5,7,8,10,12):
        thismonth += 31
    elif n in (4,6,9,11):
        thismonth += 30
    else:
        thismonth += 28

    thismonth = thismonth % 7
M = month_numbers[month-1]

Leapyear = 0
fullyear = int(fullyear)
if fullyear % 400 == 0:
    Leapyear = 1
elif fullyear % 4 == 0 and fullyear % 100 != 0:
    Leapyear = 1

if Leapyear == 1 and month <= 2:
    W = (C + Y + M + day - 1) % 7
else:
    W = (C + Y + M + day) % 7

weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
print(weekdays[W])
    
