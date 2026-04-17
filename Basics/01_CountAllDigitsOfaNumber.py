#Brute Force approach

num = 12345

# count = 0

# while num > 0:
#     count = count+1
#     n = num%10
#     num = num//10

# print(count)

# Optimal Approach

import math

def counter(num):
    count = int(math.log10(num)+1)

    return count

result = counter(num)
print(result)