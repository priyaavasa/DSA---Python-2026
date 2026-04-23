#Brute Force

num = 5
'''
def prime(num):
    count =0
    if(num < 2):
        return false
    else:
        for i in range(1, num+1):
            if(num%i==0):
                count+=1
    return count
'''

#Optimal 
import math

def prime(num):
    count =0
    if(num < 2):
        return false
    else:
        for i in range(1, math.isqrt(num)+1):
            if(num%i==0):
                count+=1

    return count

result = prime(num)
print(result==2)