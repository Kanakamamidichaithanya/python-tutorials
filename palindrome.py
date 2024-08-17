a = 121
temp = a
rev = 0
while temp > 0:
    rem = temp % 10
    rev = rev * 10 + rem
    temp = temp //10
if a ==  rev:
    print("is aplindrome")
else :
    print("not a palindrome")


