first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))

if first > second:
    print(f"{first} is bigger than {second}")
elif second > first:
    print(f"{second} is bigger than {first}")
else:
    print(f"{first} and {second} are equal")
