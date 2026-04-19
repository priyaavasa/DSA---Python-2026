n = 36

def divisors(n):
    res = []
    for i in range(1,n+1):
        if(n%i==0):
            res.append(i)

    return res

result = divisors(n)
print(result)
