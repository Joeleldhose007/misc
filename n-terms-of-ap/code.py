first = int(input("Enter the first term of AP: "))
cd = int(input("Enter the common difference of AP: "))
limit = int(input("Enter the limit of AP: "))

for i in range(limit):
    print(first+cd*i)
