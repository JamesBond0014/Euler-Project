n = 20

a = [0] * (n+1)
paths = []
for i in range(n+1):
    paths.append(a)

for x in range(n+1):
    for y in range(n+1):
        if (x ==0 or y ==0):
            paths[x][y] = 1
        else:
            paths[x][y] = paths[x-1][y] + paths[x][y-1]
print(paths[n][n])