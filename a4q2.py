year = int(input("Enter a year:"))
9
if year%400 == 0:
    print("Leap year")
elif year%100 == 0:
    print("Not leap year")
elif year%4 == 0:
    print("Leap year")
else:
    print("Not leap year")