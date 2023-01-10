x = int(input("Enter the numer to find raised to of:"))
y = int(input("Enter the numer to raise by:"))
temp = x
for i in range(y):
    temp = temp*x
    print(temp)
print("x^y = ", temp)
