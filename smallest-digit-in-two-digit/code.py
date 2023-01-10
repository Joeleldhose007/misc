num = int(input("Enter the 2 digit number to find the smallest digit of: "))
rem = num % 10

if rem < (num-rem)/10:
    print(f"{rem} is smallest digit in {num}")
elif rem > (num-rem)/10:
    print(f"{(num-rem)/10} is smallest digit in {num}")
else:
    print("Both digits are equal!")
