def DecimalToBinary(decimal):
    print(decimal,"dfd")
    if decimal > 1:
        DecimalToBinary(decimal // 2)
    print(decimal % 2, end='')

decimal = int(input("Enter a decimal number :"))
DecimalToBinary(decimal)