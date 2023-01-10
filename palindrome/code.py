num = int(input("Enter the number to reverse: "))
sign = 1
rev = 0
temp = num
if num < 0:
    sign = -1
    temp = abs(num)
while temp != 0:
    rev = rev*10 + temp % 10
    temp = temp//10

if num == rev:
    print(f"{num} is palindrome!")
else:
    print(f"{num} is not palindrome!")
