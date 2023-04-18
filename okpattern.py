str="";    
for Row in range(0,7):    
    for Col in range(0,7):     
        if (((Col == 1 or Col == 5) and Row != 0 and Row != 6) or ((Row == 0 or Row == 6) and Col > 1 and Col < 5)):  
            str=str+"*"    
        else:      
            str=str+" "    
    str=str+"\n"    
print(str);    

for i in range(7):
    for j in range(7):
        if j == 0 or i - j == 3 or i + j == 3:
            print("*", end="")
        else:
            print(end=" ")
    print()

