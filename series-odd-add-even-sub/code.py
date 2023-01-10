def sum(n):
    s = 0
    for i in range(1, n + 1):
        s += (-1) ** (i + 1) * i ** 2
    return s

n = int(input("Enter the number of terms: "))
print("Sum of series upto", n, "terms:", sum(n))
