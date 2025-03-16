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



# def add(a,b):
#     return a + b
  
# def subract(a,b):
#     return a - b
    
# def multiply(a,b):
#    return a * b
 
# def divide(a,b):
#    return a / b
 

# print("enter the operation:\n" \
# "1.add\n" \
# "2.subract\n" \
# "3.multiplication\n" \
# "4.divide")

# option_select = int(input("enter you option for operation "))
# a = int(input("enter the first number"))
# b = int(input("enter the second number"))
# if option_select == 1:
#     result = add(a, b)
#     print(f"The result of addition is: {result}")
# elif option_select == 2:
#     result = subract(a, b)
#     print(f"The result of subtraction is: {result}")
# elif option_select == 3:
#     result = multiply(a, b)
#     print(f"The result of multiplication is: {result}")
# elif option_select == 4:
#     result = divide(a, b)
#     print(f"The result of division is: {result}")
# else:
#     print("Invalid option. Please select a valid operation.")



# with open("weather_data.csv") as data_file:
#     data= data_file.readlines()
# print(data)



# a = int(input("enter a number"))
# if (a %2 == 0):
#     print("even number")
# else:
#     print("not a even number")    



# a = int(input("enter a number"))
# if (a %2 != 0):
#     print("odd number")
# else:
#     print("not a odd number")   


# a =int(input("Enter a number"))
# for i in range(2,a):
#     if (a % i == 0):
#         print("not a prime number")
#         break
#     else:
#         print("prime number")


# a = 121
# temp = a
# rev = 0
# while temp>0:
#     rem = temp%10
#     rev = rev * 10 + rem
#     temp = temp// 10
# if (a == rev):
#     print("palindrome")
# else:
#     print("not a palindrome")    


# num = 153
# temp = num
# arm = 0
# while temp>0:
#     rem = temp % 10\

#     arm = arm + (rem *rem*rem)
#     temp = temp//10
# if (num == arm):
#     print("is a armstrong")
# else:
#     print("not a arm")


# a = 0
# b = 1    
# n = 5
# while n > 0:
#     print(a)
#     c = a+b
#     a = b
#     b = c
#     n = n-1


# class Employee:
#     def __init__(self,name,sal):
#         self.name = name
#         self.sal = sal
#     def display(self):
#         print(f"salari is{self.sal} and name is is{self.name}")    
# e1 = Employee("chaithu", 250000,)
# e2 = Employee("naani" , 400000)

# e1.display()


# class Person():
#     def __init__(self):
#         self.name = "chaithu"
#         self.age = 20
# class Parent(Person):
#     def __init__(self):
#         super().__init__()
#         self.job = "manager"
#     def __str__(self):
#         return f"Parent(Name: {self.name}, Age: {self.age}, Class: {self.clss})"
# class Student(Person):
#     def __init__(self):
#        super().__init__()
#        self.clss = "tenth"
#     def __str__(self):
#         return f"Student(Name: {self.name}, Age: {self.age}, Class: {self.clss})"

# s1 = Student()
# print(s1)

# p1 = Parent()
# print(p1)






# class Job(object):
#     def __init__(self,job_name):
#         self.job_name = job_name
# class Salary(object):
#     def __init__(self,sal):
#         self.salary = sal
# class Employee(Job,Salary):
#     def __init__(self,name,job_name,sal):
#         Job.__init__(self,job_name)
#         Salary.__init__(self,sal)
#         self.name = name
# e1 = Employee("chaithu", "manager", 40000)
# print(e1.__dict__)


# Assuming the Person class is already defined as follows:


# class Person():
#     def __init__(self,firstname,lastname,idnumber):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.idnumber = idnumber
#     def display(self):
#         print(f"name is {self.firstname + self.lastname} and id is {self.idnumber}")
# class Student(Person):
#     def __init__(self,firstname,lastname,idnumber,marks):
#         super().__init__(firstname,lastname,idnumber)
#         self.marks = marks
#     def calculate(self):
#         avg = sum(self.marks) / len(self.marks)
#         if avg >= 90:
#             return 'O'  # Outstanding
#         elif avg >= 80:
#             return 'E'  # Exceeds Expectations
#         elif avg >= 70:
#             return 'A'  # Acceptable
#         elif avg >= 55:
#             return 'P'  # Poor
#         elif avg >= 40:
#             return 'D'  # Dreadful
#         else:
#             return 'T'  # Troll
        
# s1 = Student("kanaka","chaithu", 35 , [12,13,14,15])
# s1.calculate()
# print(f"Grade: {s1.calculate()}")


# class Book:
#     def __init__(self,title,pages):
#         self.title=title
#         self.pages=pages
#     def __add__(self, other,next):
#         total=self.pages+other.pages
#         return total
# b1=Book('One indian girl', 300)
# b2=Book('making india awesome',200)
# b3=Book('half girlfriend', 400)
# print("total number of pages", b1+b2+b3)


# class Vehicle:
   
#     def __init__(self, name, max_speed, mileage, color = 'white'):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#         self.color = color

# class Bus(Vehicle):
#     pass

# class Car(Vehicle):
#     pass

# b1=Bus('ai', 120, 2000)
# print(b1.__dict__)



# n = int(input("enter number:"))
# power = len(str(n))
# temp = n
# arm = 0
# while temp > 0:
#     rem = temp % 10
#     arm = arm + (rem**power)
#     temp = temp//10
# if  n == arm:
#     print("is arm")
# else :
#     print("not not arm")          

# import numpy as np
# array = np.random.randint(0,25,10)
# max = np.max(array)
# index = array.argmax()
# print(array)
# print(max)
# print(index)
# # shape = (array.reshape(2,5))
# # print(shape)

# import numpy as np
# array = np.arange(1,11)
# slice_of_array = array[0:6

# print(slice_of_array)
# print(array)

# import numpy_test as np
# array = np.arange(50).reshape(5,10)
# # print(array)
# sub=(array[1:4])
# # print(sub)
# sub2 = sub[0:,1:4]
# print(sub2)

