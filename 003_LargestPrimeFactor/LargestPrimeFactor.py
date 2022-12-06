import math
def GetAllPrimeFactors(n):
    factors = list()
    while (n % 2) == 0:
        factors.append(2)
        n = int(n/2)
    for i in range(3,math.ceil(math.sqrt(n)+1), 2):
        if (n % i) == 0:
            factors.append(i)
            n = int(n/i)
    if n > 1:
        factors.append(n)
    return factors

result = GetAllPrimeFactors(600851475143)
result.sort(reverse=True)
print(result[0])