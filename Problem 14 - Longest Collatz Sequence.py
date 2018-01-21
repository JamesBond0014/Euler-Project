def collatz(n,d):
    
    count = 1
    temp = n
    while (temp != 1):
        if (temp in d):
            count += d[temp]
            return count
        if (temp%2 == 0):
            temp = temp//2
        else:
            temp = temp*3 +1
        count +=1
    return count
max_val = 1000000
answer = 0
answer_len =0
d = {}
for i in range(1,max_val+1):
    
    collatz_len = collatz(i, d)
    if (collatz_len > answer_len):
        answer_len = collatz_len
        answer = i
    
    d[i] = collatz_len

print(answer)
    