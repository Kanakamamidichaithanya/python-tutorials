#basic recursive function programs
# def show(n):
#     if (n==0):
#         return
#     print(n)
#     show(n-1)
# show (5)        


#finding factorial using recurssive function
# def fact(n):
#     if (n==0 or n==1):
#         return 1
#     return fact (n-1) * n
# print(fact(5))


#recursive function to find sum of n natural numbers
# def sum(n):
#     sum = 0
    
#     if (n == 0):
#         return 0
#     for i in range(1,n+1):
#         sum = sum + i
        
       
#     print(sum)
# sum(3) 



                             #(or)

# def sum(n):
#     if (n==0):
#         return 0
#     # print(n)
#     # sum(n-1)
#     return sum(n-1) + n
# total_sum = sum(5)
# print(total_sum)
  
 
 
#adding elements in list using recursion
# def addlist(elements):
#     if (elements == []):
#         return 0
#     else:
#         return elements[0] + addlist(elements[1:])
# list = [1,2,3,4,5]
# totaladd = addlist(list)
# print(totaladd)


# def convertint(intgr):
#     if (intgr == 0):
#         return "0"
#     else :
#         return str(intgr)
# intgr = 1231
# string = convertint(intgr)
# print(string)    


#recusion for nested list
# def listsum(list):
#     total = 0
#     for element in list:
#         if (type (element) == type([])):
#             total = total + listsum(element)
#         else :
#             total = total + element
#     return total
# list = [1,2,[1,2],[1,3]]
# totalsum = listsum(list)
# print(totalsum)   




#factorial using recursion
# def factorial(n): 
    
#     for i in range(1,n+1):
#         if (n==1 or n==0):
#             return 1
#         else :
#             return n * factorial(n-1)
# print(factorial(5))


#finding fibonocci using recursion
def fib(n):
    a = 0
    b = 0
    while n > 0:
        return 