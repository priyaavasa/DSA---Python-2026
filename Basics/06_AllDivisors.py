n = 36

#Brute Force approach
"""
def divisors(n):
    res = []
    for i in range(1,n+1):
        if(n%i==0):
            res.append(i)

    return res
"""
#Optimal

import math

def divisors(n):
    res = []
    for i in range(1,math.isqrt(n) + 1):
        if(n%i==0):
            res.append(i)

        if i != n // i:
            res.append(n // i)
    return res


result = divisors(n)
print(result)
