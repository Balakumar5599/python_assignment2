inp_num=input()
list1=[]
for i in inp_num:
    list1.append((i))
list1.sort(reverse=True)
s=''
for x in list1:
    s=s+x
print(s)
#print(list1)
