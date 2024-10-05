# # def greet(name):
# #     print("hello",name)
# # greet("chaithu")    
# # import math
# def cans_required(height,width):
#   coveragepercan = 5
#   total_cans_required = round((height*width)/coveragepercan)
#   print(f"You'll need {total_cans_required} cans of paint")

# test_h = int(input("height:")) # Height of wall (m)
# test_w = int(input("width:")) # Width of wall (m)    
# cans_required(height=test_h,width=test_w) 


  

# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# # 🚨 Don't change the code above 👆
# # TODO-1: Create an empty dictionary called student_grades.
# grades = {}

# # TODO-2: Write your code below to add the grades to student_grades.👇
# for students in student_scores:
#     student_grades = student_scores[students]
#     if (student_grades > 90):
#       print("Outstanding")
#     elif (student_grades > 80 and student_grades < 90):
#        print("Exceeds Expectations") 
#     elif (student_grades > 7 and student_grades < 80):  
#        print( "Acceptable")  
#     elif(student_grades<= 70) :
#        print("Fail")   

# # 🚨 Don't change the code below 👇




# country = input("enter country") # Add country name
# visits = int(input("enter no of visits")) # Number of visits
# cities = (input("enter the cities")) # create list from formatted string
# cities_input.split(", ")

# travel_log = [
#   {
#     "country": "France",
#     "visits": 12,
#     "cities": ["Paris", "Lille", "Dijon"]
#   },
#   {
#     "country": "Germany",
#     "visits": 5,
#     "cities": ["Berlin", "Hamburg", "Stuttgart"]
#   },
# ]
# def new_country(country, visits,cities ):
#     new_country={}
#     new_country["country"] = country
#     new_country["visits"] = visits
#     new_country["cities"] = cities
#     travel_log.append(new_country)
#     print(travel_log) 
       

# new_country(country, visits, cities)
# print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
# print(f"My favourite city was {travel_log[2]['cities'][0]}.")



# country = input() # Add country name
# visits = int(input()) # Number of visits
# list_of_cities = eval(input()) # create list from formatted string
# travel_log = [
#   {
#     "country": "France",
#     "visits": 12,
#     "cities": ["Paris", "Lille", "Dijon"]
#   },
#   {
#     "country": "Germany",
#     "visits": 5,
#     "cities": ["Berlin", "Hamburg", "Stuttgart"]
#   },
# ]
# # Your code here 👇
# def add_new_country(name, times_visited, cities_visited):
#   new_country = {}
#   new_country["country"] = name
#   new_country["visits"] = times_visited
#   new_country["cities"] = cities_visited
#   travel_log.append(new_country)

# add_new_country(country, visits, list_of_cities)
# print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
# print(f"My favourite city was {travel_log[2]['cities'][0]}.")



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