num = 123
temp = num 

def armstrong(num):
    count = len(str(num))

    arm = 0
    while num>0:
        n = num%10 
        arm = arm + (n**count)
        num = num//10
    return arm

result = armstrong(num)

print(result==temp)