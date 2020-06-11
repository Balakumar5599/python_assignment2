# Difference Between break, continue, pass:-

#Break statement

name=input("Enter name for executing break statement: ")

for letter in name:
    if letter== 'm'or letter=='h':
        break      #It will break the loop, when the if condition is satisfied.
    print(letter)
print("Exit from the for loop")

number=15

for num in range(0,number):
    if num==5:
        break      #It will break the loop, when num is equal to 10.
    print(num)
print("Exit from the for loop")


#Continue statement

n=int(input("Enter number for executing continue statement: "))
    
for i in range(0,n):
    if i==3:
        continue   #If condition is satisfied, continue to next iteration without printing.
    print(i)


#Pass statement

name=input("Enter name for executing pass statement: ")
num=int(input("Enter number for executing pass statement: "))

for letter in name:
    pass

for number in range(0,10):
    if number==5:
        pass       #It allows us to handle the condition without the loop being impacted in any way.
    print(number)

def funct():
    pass
