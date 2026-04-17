num = 123

def reverse(num):
    revnum = 0

    while num>0:
        n = num % 10
        revnum = revnum*10+n
        num = num//10 

    return revnum

result = reverse(num)
print(result)