# 2. Get the total number of rows to be printed from the user input and print the pattern:-

#Method-1

num_of_row=int(input("Enter the number of rows: "))

for row in range(0,num_of_row):
    
    if row<=num_of_row//2:
        
        print("*"*(row+1)+"*"*(row),end="")
        print()
        ref_num=row+1
        
    if row>num_of_row//2:
        
        print("*"*(ref_num-1)+"*"*(ref_num-2),end="")
        print()
        ref_num-=1
        
        
#Method-2 Using function

def arrow_pattern(num_of_row):
    
    for row in range(0,num_of_row):
    
        if row<=num_of_row//2:
        
            print("*"*(row+1)+"*"*(row),end="")
            print()
            ref_num=row+1
        
        if row>num_of_row//2:
            
            print("*"*(ref_num-1)+"*"*(ref_num-2),end="")
            print()
            ref_num-=1

num_of_row=int(input("Enter the number of rows: "))
arrow_pattern(num_of_row)

    
