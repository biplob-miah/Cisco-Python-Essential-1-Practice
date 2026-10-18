'''year =int(input("Enter the year from 1582 to check :"))
if year < 1582:
    print("Not within the Gregorian calendar")

elif year % 400 == 0:
    print(year, "is leap year")
    
elif year % 100 == 0:
    print(year, "is leap year")

elif year % 4 == 0:
    print(year, "is leap year")

else:
    print(year, "is common year")

'''

year =int(input("Enter the year from 1582 to check :"))
if year < 1582:
    print("Not within the Gregorian calendar")
else:
    if year % 400 != 0:
        print(year, "is common year")
    elif year % 100 !=0:
        print(year, "is common year")
    elif year % 4 !=0:
        print(year, "is common year")
    else:
        print(year, "is leap year")
