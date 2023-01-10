num = int(input("Enter the number to find the sum of the factors of: "))
sum = 0
for i in range(1, num+1):
    if num % i == 0:
        sum += i

print("Sum of factors = ", sum)
