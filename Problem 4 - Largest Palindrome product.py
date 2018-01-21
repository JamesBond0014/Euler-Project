def isPal(x):
    y = str(x)
    length = len(y)//2
    for i in range(length):
        if (y[i] != y[-i-1]):
            return False

    return True
pal = 0
x = 999
y = 999
while (1):
    if isPal(x*y):
        if (pal < x*y):
            pal = x*y
    
    x -=1
    if (x == 0):
        y -= 1
        x = y
        if (y ==0):
            break
print(pal)