num = int(input("Enter the number to reverse: "))
sign = 1
rev = 0
if num < 0:
    sign = -1
    num = abs(num)
while num != 0:
    rev = rev*10 + num % 10
    num = num//10

print(sign*rev)
