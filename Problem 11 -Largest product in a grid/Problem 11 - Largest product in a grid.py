file = open("input.txt","r")
f = []
for i in range(20):
    f.append(file.readline().strip().split())
file.close

for i in range(len(f)):
    for k in range(len(f[i])):
        f[i][k] = int(f[i][k])

max_val = 0
for k in range(len(f)):
    for i in range(2,len(f[k])-1):
        temp = f[k][i-2]*f[k][i-1]*f[k][i]*f[k][i+1]
        if temp>max_val:
            max_val = temp

for i in range(len(f)):
    for k in range(2,len(f)-1):
        temp = f[k-2][i]*f[k-1][i]*f[k][i]*f[k+1][i]
        if temp>max_val:
            max_val = temp


for i in range(len(f)-4):
    for k in range(len(f)-4):
        temp = f[k][i]*f[k+1][i+1]*f[k+2][i+2]*f[k+3][i+3]
        if temp>max_val:
            max_val = temp
for i in range(3,len(f)):
    for k in range(len(f)-4):
        temp = f[k][i]*f[k+1][i-1]*f[k+2][i-2]*f[k+3][i-3]
        if temp>max_val:
            max_val = temp
print(max_val)