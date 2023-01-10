x1 = int(input("Enter the first x coordinate: "))
x2 = int(input("Enter the second x coordinate: "))

if x1 > 0 and x2 > 0:
    if x1 > x2:
        distance = x1-x2
    else:
        distance = x2-x1

else:
    if x1 > x2:
        distance = x1-x2
    else:
        distance = x2-x1

print(f"Distance between {x1} and {x2} is {distance}")
