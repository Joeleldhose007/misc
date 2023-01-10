def gcd(a, b):
    if b > a:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a


first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
print("The GCD of", first, "and", second, "is", gcd(first, second))
