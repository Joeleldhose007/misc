first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))

if first % second == 0:
    print(f"{second} is multiple of {first}")
else:
    print(f"{second} is not a multiple of {first}")
