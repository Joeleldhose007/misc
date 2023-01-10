first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
third = int(input("Enter the third number: "))

if first < second and first < third:
    print(f"{first} is smallest")
elif second < first and second < third:
    print(f"{second} is smallest")
elif third < first and third < second:
    print(f"{third} is smallest")
else:
    print("All three numbers are equal")
