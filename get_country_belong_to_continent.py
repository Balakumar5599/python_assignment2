# 3. Print all the country names that belong to a certain continent from a given dictionary:-

len_of_dict=int(input("Enter the length of dictionary: "))
print("Enter the keys and values of the dictionary seperated by colon: ")
input_dict={}
for dict_item in range(0,len_of_dict):
    key,value=input().split(":")
    input_dict[key]=value
print(input_dict)
continent=input("Enter the continent name: ")
print("Countries that belongs to the continent: ")
for key,value in input_dict.items():
    if continent==value:
        print(key,end=" ")



print()
print()
#Method-2 using function:-

def get_country(given_dict):

    continent=input("Enter the continent name: ")
    print("Countries that belongs to the continent: ")
    for key,value in given_dict.items():
        if continent==value:
            print(key,end=" ")

given_dict={'Spain':'Europe','Japan':'Asia','India':'Asia','Italy':'Europe','Thailand':'Asia','Sudan':'Africa'}

get_country(given_dict)
    
    
