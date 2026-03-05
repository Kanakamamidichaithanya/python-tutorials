# a = 121
# temp = a
# rev = 0
# while temp > 0:
#     rem = temp % 10
#     rev = rev * 10 + rem
#     temp = temp //10
# if a ==  rev:
#     print("is aplindrome")
# else :
#     print("not a palindrome")

def ispalindrome(number):
    temp = number
    rev = 0
    while temp > 0:
        rem = temp % 10
        rev = rev * 10 + rem
        temp = temp //10
    return number == rev
number = int(input("enter a number"))
if ispalindrome(number):
    print("is a palindrome")
else:
    print("not a palindrome")
number = int(input("enter a number"))
