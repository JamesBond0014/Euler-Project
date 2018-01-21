def factor(num):
    a = {}
    x = 1
    while(1):
        x+=1
  
        if (num%x ==0):
            
            num = num//x
            if (x in a):
                a[x] +=1
            else:
                a[x] = 1
            x -= 1
        if (num == 1 or x>num):
            break
    return a   
d = {}
for i in range(20):

    a = factor(i+1)
    print(a)
    for k in a:
        if (k in d):
            if (a[k]>d[k]):
                d[k] = a[k]
        else:
            d[k] = a[k]
print(d)
total = 1
for i in d:
    total *= i**d[i] 
print(total)