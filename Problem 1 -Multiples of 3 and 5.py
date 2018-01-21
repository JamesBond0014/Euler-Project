def sum(x):
    return (x*(x+1))//2

upper = 1000-1

count3 = upper//3
count5 = upper//5
count15 = upper//15
total3 = sum(count3)
total5 = sum(count5)
total15 = sum(count15)

print(total3*3+total5*5 - total15*15)