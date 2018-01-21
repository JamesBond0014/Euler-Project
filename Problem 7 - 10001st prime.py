prime = 10001
curr = 1
primes = []
def isPrime(x, a):
    for i in a:
        if x%i == 0:
            return False
    return True

while (len(primes) < prime):
    curr+=1
    
    if (isPrime(curr, primes)):
        primes.append(curr)
print(primes[-1])