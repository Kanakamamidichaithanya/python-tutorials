a = 153
temp = a 
arm = 0
n = len(str(a))
while temp > 0:
    rem = temp % 10
    arm = arm + (rem**n)
    temp = temp//10
if  a == arm:
    print("is arm")
else :
    print("not not arm")          


# def isarmstrong(number):
#     temp = number
#     arm = 0
#     num_digits = len(str(number))
#     rem = temp % 10
#     arm = arm + rem ** num_digits
#     temp = temp//10
#     return arm
# number = int(input("enter a number"))
# if isarmstrong(number):
#     print("is a arm")



# def armstrong(number):
#     temp = number
#     arm = 0
#     n = len(str(number))
#     while temp>0:
#         rem = temp%10
#         arm = arm + (rem**n)
#         temp = temp // 10

#     if arm == number:
#         print(number, "is an Armstrong Number")
#     else:
#         print(number, "is NOT an Armstrong Number")

# num = 121
# armstrong(num)


# def armstrong(number):
#     temp = number
#     n = len(str(number))
#     arm = 0

#     while temp > 0:
#         rem = temp % 10
#         arm = arm + (rem ** n)
#         temp = temp // 10

#     if arm == number:
#         print(number, "is an Armstrong Number")
#     else:
#         print(number, "is NOT an Armstrong Number")


# num = int(input("Enter a number: "))
# armstrong(num)