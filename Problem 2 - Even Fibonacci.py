x = 1
y = 2

total = 2
new = x+y
while (1):
    x = y
    y = new
    new = x+y
    
    if (new>4000000):
        break
    if (new%2==0):
        total += new

print (total)