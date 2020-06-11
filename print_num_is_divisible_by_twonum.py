# 1. The numbers that are completely divisible for the given range:-

range_from=int(input("Enter the range value from: "))
range_to=int(input("Enter the range value to: "))
print("The Numbers that are completely divisible for the given range are: ")

for value in range(range_from,range_to+1):
    if value%75==0 and value%100==0:
        print(value)
