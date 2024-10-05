def add(a,b):
    return a + b
  
def subract(a,b):
    return a - b
    
def multiply(a,b):
   return a * b
 
def divide(a,b):
   return a / b
 

print("enter the operation:\n" \
"1.add\n" \
"2.subract\n" \
"3.multiplication\n" \
"4.divide")

option_select = int(input("enter you option for operation "))
a = int(input("enter the first number"))
b = int(input("enter the second number"))
if option_select == 1:
    result = add(a, b)
    print(f"The result of addition is: {result}")
elif option_select == 2:
    result = subract(a, b)
    print(f"The result of subtraction is: {result}")
elif option_select == 3:
    result = multiply(a, b)
    print(f"The result of multiplication is: {result}")
elif option_select == 4:
    result = divide(a, b)
    print(f"The result of division is: {result}")
else:
    print("Invalid option. Please select a valid operation.")