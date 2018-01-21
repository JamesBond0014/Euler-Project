def factor(x,a):
    if x == 1 or x == 0:
        return a
    for i in range(2, x+1):
        if x%i==0:

            if i in a:
                a[i] +=1
            else:
                a[i] = 1
            x = x//i
            break
    return factor(x, a)

def mergegreatkey(d,e):
    for i in d:
        if i in e:
            if d[i] > e[i]:
                e[i] = d[i]
        else:
            e[i] = d[i]
    
    return e

df= {1:1}
c={1:1}
b={1:1}

for i in range(21):
    print(i)
    b = factor(i,df)
    print("B:",b)
    c = mergegreatkey(b,c)
    print("C:",c)
    b.clear()
final = 1
for i in c:
    final = final*pow(i,c[i])

print(final    )
    