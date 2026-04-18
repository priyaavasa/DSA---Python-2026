num = 1217
temp = num
def palindrome(num):
    result = 0
    while num>0:
        n = num%10
        result= result*10+n
        num = num//10

    return result

pal = palindrome(num)
print(pal==temp)
# if(temp == pal):
#     print("Palindrome")
# else:
#     print("Not a Palindrome")
