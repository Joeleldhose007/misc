num = int(input("Enter the number to check: "))
temp = num
sum = 0
while temp != 0:
    rem = temp % 10
    sum = sum + rem * rem * rem
    temp = temp / 10

if sum == num:
    print(f"{num} is a armstrong number!")
else:
    print(f"{num} is not a armstrong number!")
