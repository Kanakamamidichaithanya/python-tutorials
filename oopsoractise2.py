# class student:
#     name = "chaithanya"
# s1 = student                    deleting a object
# del s1.name
# print(s1.name)


# class Account:
#     def __init__ (self,acc_no,acc_pass):
#         self.account_number = acc_no
#         self.account_password = acc_pass
# a1 = Account(1234,"abcd")  
# print(a1.account_number,a1.account_password)


# class car:
#     @staticmethod
#     def start():
#         print("car is started..")
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
# class specifications(car):
#     def __init__(self,color,model):
#         self.color = color
#         self.model = model
        

# # car.start() 
# # c1 = car("toyota", "fortuner")
# # print(c1.brand,c1.model)

# c2 = specifications("black", "sigmafour")
# print(c2.color,c2.model)



# class car:
#     colour = "black"
#     @staticmethod
#     def start():
#         print("car is started..")
#     @staticmethod
#     def stop():                            example for single inheritance
#         print("car is stopped..")
# class suzuki(car):
#     def __init__(self,name):
#         self.name = name
# c1 = suzuki("swift")
# print(c1.colour)




# class car:
#     colour = "black"
#     @staticmethod
#     def start():
#         print("car is started..")
#     @staticmethod
#     def stop():                           
#         print("car is stopped..")
                                                  #example for multilevel inheritance
# class suzuki(car):
#     def __init__(self,name):
#         self.name = name
# class baleno(suzuki):
#     def __init__(self,type):
#         self.type = type
# c1 = suzuki("kerosene")
# c1.start()     




# class A:
#     var1 = "welcome to class a"
# class B:
#     var2 = "welcome to class b"
# class C(A,B):                           example for mulipath inheritance
#     var3 = "welcome to class c"

# c1 = C()
# print(c1.var1)
# print(c1.var2)
# print(c1.var3)



# #finding average marks of a student and changinf after using "@property" method
# class student :
#     def __init__(self,chem,math,phy):
#         self.chem = chem
#         self.math = math
#         self.phy = phy
#     @property
#     def calc_avg(self):
#         return str((self.chem+self.math+self.phy)/3)+ "%"
# s1 = student(98,87,99)
# print(s1.calc_avg)

# s1.math = 60
# print(s1.calc_avg)

# s1.phy = 100
# print(s1.calc_avg)



#adding to complex numbers using method over loading and dunder functions
# class complex:
#     def __init__(self,real,img):
#         self.real = real
#         self.img = img
#     def 
#     def __d(self,new2):
#         self.real = self.real + new2.real
#         self.img = self.img + new2.img
#         print(self.real ,"+", self.img)

# new1 = complex(2 , 3)
# print(new1.complex)        



# two_digit_number = input("enter any two digit number")
# sumdig = 0
# i = 0
# while i< len(two_digit_number):
#   sumdig += int(two_digit_number[i])
#   i+=1
# print(sumdig)

# import random
# randon_integer = random.randint(1,12)
# print(randon_integer)



# fruits1 = ['apple', 'banana', 'cherry']
# fruits2 = ['grape', 'cust', 'pine']
# totalfruits = [fruits1, fruits2]

# # Access the position of 'grape'
# position_in_sublist = totalfruits[1].index('cust')
# print("Position of 'cust' in the second list:", position_in_sublist)

# class Car:
#     def set_brand(self, brand):  # 'self' refers to the current object
#         self.brand = brand  # Store brand inside the object
    
#     def show_brand(self):
#         print(f"The car brand is {self.brand}")

# class student:
#     def __init__(self,name,rollnumber):
#         self.name = name
#         self.rollno = rollnumber
#     def details(self):
#         print(f"name is : ({self.name} and rollno is : {self.rollno})")
# student1 = student("chaithu", "21911A6735")
# student1.details()        


# class Person:
#     def __init__(self,name,age,gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#     def introduce(self):
#         return f"My name is {self.name}, I am {self.age} years old, {self.gender}."
# class Student(Person):
#     def __init__(self,name,age,gender,grade):
#         super().__init__(name,age,gender)
#         self.grade = grade
#     def introduce(self):
#         return super().introduce() + f"I study in grade {self.grade}"
# class Teacher(Person):
#     def __init__(self,name,age,gender,subject):
#         super().__init__(name,age,gender)
#         self.subject = subject
#     def introduce(self):
#         return super().introduce() + f"i teach {self.subject}"
# student = Student("chaithanya",20,"male",10)
# print(student.introduce())
# teacher = Teacher("chaithu", 30, "male", "maths")
# print(teacher.introduce())
        
        
# class Vehicle:
#     def __init__(self,brand,model,year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#     def vehicle_info(self):
#         return f"Vehicle: {self.brand} {self.model} ({self.year})"
# class Car(Vehicle):
#     def __init__(self,brand,model,year,fuel_type):
#         super().__init__(brand,model,year)
#         self.fuel_type = fuel_type
#     def vehicle_info(self):
#         return super().vehicle_info() + f"fuel type : {self.fuel_type}"
# car = Car("toyota","fortuner",2000,"petrol")
# print(car.vehicle_info())
        
# from abc import ABC,abstractmethod
# class Payment:
#     @abstractmethod
#     def process_payment():
#         pass
#     def transaction_details():
#         pass
    

# from math import pi
# class shape:
#     def area(self):
#         pass
# class Rectangle(shape):
#     def __init__(self,width,height):
#         self.width = width
#         self.height = height
#     def area(self):  # Overriding area method
#         return self.width * self.height
# class Circle(shape):
#     def __init__(self,radius):
#         self.radius = radius
#     def area(self):
#         return pi * self.radius * self.radius
# rect = Rectangle(24,2)
# print(f"Rectangle Area: {rect.area()}")
# cir = Circle(4)
# print(cir.area())

# class Employee:
#     def calculate_salary(self):
#         pass
# class Fulltme_employee(Employee):
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
#     def calculate_salary(self):
#         return f"{self.name} earns {self.salary} per month"
# class Partime_employee(Employee):
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
#     def calculate_salary(self):
#         return f"{self.name} earns {self.salary} per month"
# employee = Fulltme_employee("chaithu", 500000)
# print(employee.calculate_salary()) 
# employee2 = Partime_employee("naani", 500000) 
# print(employee2.calculate_salary())  


# class BankAccount:
#     def __init__(self, account_number, balance):
#         self.__account_number = account_number  # Private attribute
#         self.__balance = float(balance)  # Convert balance to float

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             return "Deposit successful"
#         else:
#             return "Invalid deposit amount"

#     def withdraw(self, amount):
#         if amount <= self.__balance:  # Allow withdrawal if amount is <= balance
#             self.__balance -= amount
#             return "Withdrawal successful"
#         else:
#             return "Withdrawal unsuccessful - Insufficient balance"

#     def get_balance(self):  # Getter method
#         return self.__balance
# # Creating an account
# account = BankAccount("123456789", 5000)

# # Depositing money
# print(account.deposit(1500))  # Output: "Deposit successful"
# print(account.get_balance())  # Output: 6500

# # Withdrawing money
# print(account.withdraw(2000))  # Output: "Withdrawal successful"
# print(account.get_balance())   # Output: 4500

# # Trying to withdraw more than balance
# print(account.withdraw(5000))  # 