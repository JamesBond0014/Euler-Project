file = open("input.txt",'r')
f = file.readlines()
file.close()

total = 0
for i in f:
    total +=int(i)

total = str(total)

print(total[0:10])