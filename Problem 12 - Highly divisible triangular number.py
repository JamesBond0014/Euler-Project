import math

def factor(num):
    if num == 1:
        return 1
    total = 0
    for i in range(1,math.ceil(num**0.5)):
        if (num%i ==0):
            total +=2
    return total
            
    
    

def triangle_number(i):
    return ((i*(i+1))//2)

count = 0
exit_cond = 500,
while (1):
    count+=1
    if (factor(triangle_number(count))>=exit_cond):
        print(triangle_number(count))
        break