inp_strings=input("Enter the strings ").split(",")
str1=sorted(inp_strings[0])
str2=sorted(inp_strings[1])
if str1==str2:
    print("True")
else:
    print("False")
