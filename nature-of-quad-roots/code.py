a = int(input('Enter the value of a: '))
b = int(input('Enter the value of b: '))
c = int(input('Enter the value of c: '))

disciminant = b**2 - (4*a*c)
print("The disciminant value of a quadratic equation = ", disciminant)
if disciminant > 0:
    print("The roots of a quadratic equation are Real")
if disciminant == 0:
    print("The roots of a quadratic equation are Equal")
if disciminant < 0:
    print("The roots of a quadratic equation are Imaginary")
