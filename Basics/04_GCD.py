n1 = 9
n2 = 12

# Brute Force
"""
def gcd(n1,n2):
    count = 1
    minGcd = min(n1,n2)

    for i in range(1,minGcd+1):
        if n1%i==0 and n2%i==0:
            count =  i

    return count
"""

#Better
"""
def gcd(n1,n2):
    minGcd = min(n1,n2)

    for i in range(minGcd+1,0,-1):
        if n1%i==0 and n2%i==0:

            return i
"""

#Optimal

def gcd(n1, n2):
    if n1 == n2:
        return n1
    if n1 > n2:
        return gcd(n1 - n2, n2)
    else:
        return gcd(n1, n2 - n1)


result = gcd(n1,n2)
print(result)

