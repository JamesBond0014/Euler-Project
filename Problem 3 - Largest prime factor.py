number = 600851475143
x = 1
while(1):
    x+=1
    if (number%x ==0):
        number = number//x
        if (number <= 1):
            break
        x = 1
print (x)