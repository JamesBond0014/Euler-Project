def pythagoreantriplet(x):
    upper_a = x//3 - 1
    upper_b = x//2 - 1
    for i in range(upper_a):
        for k in range(upper_b):
            c = 1000 - i - k
            if (i*i + k*k == c*c):
                if (i<k and k<c):
                    return i*k*c
    return 0

print(pythagoreantriplet(1000))


