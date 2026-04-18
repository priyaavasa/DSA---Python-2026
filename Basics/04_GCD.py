n1 = 9
n2 = 12

def gcd(n1,n2):
    count = 1
    minGcd = min(n1,n2)

    for i in range(1,minGcd+1):
        if n1%i==0 and n2%i==0:
            count =  i

    return count

result = gcd(n1,n2)
print(result)

