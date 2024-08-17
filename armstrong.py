a = 153
temp = a 
arm = 0
while temp > 0:
    rem = temp % 10
    arm = arm + (rem*rem*rem)
    temp = temp//10
if  a == arm:
    print("is fib")
else :
    print("not fib")          
