def is_automorphic(n):
    return str(n**2).endswith(str(n))


n = int(input("Enter the number to check: "))
if is_automorphic(n) == True:
    print(n, " is automorphic!")
else:
    print(n, " is not a automorphic!")
