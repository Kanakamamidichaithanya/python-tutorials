# # # def greet(name):
# # #     print("hello",name)
# # # greet("chaithu")    
# # # import math
# # def cans_required(height,width):
# #   coveragepercan = 5
# #   total_cans_required = round((height*width)/coveragepercan)
# #   print(f"You'll need {total_cans_required} cans of paint")

# # test_h = int(input("height:")) # Height of wall (m)
# # test_w = int(input("width:")) # Width of wall (m)    
# # cans_required(height=test_h,width=test_w) 


  

# # student_scores = {
# #   "Harry": 81,
# #   "Ron": 78,
# #   "Hermione": 99, 
# #   "Draco": 74,
# #   "Neville": 62,
# # }
# # # 🚨 Don't change the code above 👆
# # # TODO-1: Create an empty dictionary called student_grades.
# # grades = {}

# # # TODO-2: Write your code below to add the grades to student_grades.👇
# # for students in student_scores:
# #     student_grades = student_scores[students]
# #     if (student_grades > 90):
# #       print("Outstanding")
# #     elif (student_grades > 80 and student_grades < 90):
# #        print("Exceeds Expectations") 
# #     elif (student_grades > 7 and student_grades < 80):  
# #        print( "Acceptable")  
# #     elif(student_grades<= 70) :
# #        print("Fail")   

# # # 🚨 Don't change the code below 👇




# # country = input("enter country") # Add country name
# # visits = int(input("enter no of visits")) # Number of visits
# # cities = (input("enter the cities")) # create list from formatted string
# # cities_input.split(", ")

# # travel_log = [
# #   {
# #     "country": "France",
# #     "visits": 12,
# #     "cities": ["Paris", "Lille", "Dijon"]
# #   },
# #   {
# #     "country": "Germany",
# #     "visits": 5,
# #     "cities": ["Berlin", "Hamburg", "Stuttgart"]
# #   },
# # ]
# # def new_country(country, visits,cities ):
# #     new_country={}
# #     new_country["country"] = country
# #     new_country["visits"] = visits
# #     new_country["cities"] = cities
# #     travel_log.append(new_country)
# #     print(travel_log) 
       

# # new_country(country, visits, cities)
# # print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
# # print(f"My favourite city was {travel_log[2]['cities'][0]}.")



# # country = input() # Add country name
# # visits = int(input()) # Number of visits
# # list_of_cities = eval(input()) # create list from formatted string
# # travel_log = [
# #   {
# #     "country": "France",
# #     "visits": 12,
# #     "cities": ["Paris", "Lille", "Dijon"]
# #   },
# #   {
# #     "country": "Germany",
# #     "visits": 5,
# #     "cities": ["Berlin", "Hamburg", "Stuttgart"]
# #   },
# # ]
# # # Your code here 👇
# # def add_new_country(name, times_visited, cities_visited):
# #   new_country = {}
# #   new_country["country"] = name
# #   new_country["visits"] = times_visited
# #   new_country["cities"] = cities_visited
# #   travel_log.append(new_country)

# # add_new_country(country, visits, list_of_cities)
# # print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
# # print(f"My favourite city was {travel_log[2]['cities'][0]}.")



# # def add(a,b):
# #     return a + b
  
# # def subract(a,b):
# #     return a - b
    
# # def multiply(a,b):
# #    return a * b
 
# # def divide(a,b):
# #    return a / b
 

# # print("enter the operation:\n" \
# # "1.add\n" \
# # "2.subract\n" \
# # "3.multiplication\n" \
# # "4.divide")

# # option_select = int(input("enter you option for operation "))
# # a = int(input("enter the first number"))
# # b = int(input("enter the second number"))
# # if option_select == 1:
# #     result = add(a, b)
# #     print(f"The result of addition is: {result}")
# # elif option_select == 2:
# #     result = subract(a, b)
# #     print(f"The result of subtraction is: {result}")
# # elif option_select == 3:
# #     result = multiply(a, b)
# #     print(f"The result of multiplication is: {result}")
# # elif option_select == 4:
# #     result = divide(a, b)
# #     print(f"The result of division is: {result}")
# # else:
# #     print("Invalid option. Please select a valid operation.")



# # with open("weather_data.csv") as data_file:
# #     data= data_file.readlines()
# # print(data)



# # a = int(input("enter a number"))
# # if (a %2 == 0):
# #     print("even number")
# # else:
# #     print("not a even number")    



# # a = int(input("enter a number"))
# # if (a %2 != 0):
# #     print("odd number")
# # else:
# #     print("not a odd number")   


# # a =int(input("Enter a number"))
# # for i in range(2,a):
# #     if (a % i == 0):
# #         print("not a prime number")
# #         break
# #     else:
# #         print("prime number")


# # a = 121
# # temp = a
# # rev = 0
# # while temp>0:
# #     rem = temp%10
# #     rev = rev * 10 + rem
# #     temp = temp// 10
# # if (a == rev):
# #     print("palindrome")
# # else:
# #     print("not a palindrome")    


# # num = 153
# # temp = num
# # arm = 0
# # while temp>0:
# #     rem = temp % 10\

# #     arm = arm + (rem *rem*rem)
# #     temp = temp//10
# # if (num == arm):
# #     print("is a armstrong")
# # else:
# #     print("not a arm")


# # a = 0
# # b = 1    
# # n = 5
# # while n > 0:
# #     print(a)
# #     c = a+b
# #     a = b
# #     b = c
# #     n = n-1


# # class Employee:
# #     def __init__(self,name,sal):
# #         self.name = name
# #         self.sal = sal
# #     def display(self):
# #         print(f"salari is{self.sal} and name is is{self.name}")    
# # e1 = Employee("chaithu", 250000,)
# # e2 = Employee("naani" , 400000)

# # e1.display()


# # class Person():
# #     def __init__(self):
# #         self.name = "chaithu"
# #         self.age = 20
# # class Parent(Person):
# #     def __init__(self):
# #         super().__init__()
# #         self.job = "manager"
# #     def __str__(self):
# #         return f"Parent(Name: {self.name}, Age: {self.age}, Class: {self.clss})"
# # class Student(Person):
# #     def __init__(self):
# #        super().__init__()
# #        self.clss = "tenth"
# #     def __str__(self):
# #         return f"Student(Name: {self.name}, Age: {self.age}, Class: {self.clss})"

# # s1 = Student()
# # print(s1)

# # p1 = Parent()
# # print(p1)






# # class Job(object):
# #     def __init__(self,job_name):
# #         self.job_name = job_name
# # class Salary(object):
# #     def __init__(self,sal):
# #         self.salary = sal
# # class Employee(Job,Salary):
# #     def __init__(self,name,job_name,sal):
# #         Job.__init__(self,job_name)
# #         Salary.__init__(self,sal)
# #         self.name = name
# # e1 = Employee("chaithu", "manager", 40000)
# # print(e1.__dict__)


# # Assuming the Person class is already defined as follows:


# # class Person():
# #     def __init__(self,firstname,lastname,idnumber):
# #         self.firstname = firstname
# #         self.lastname = lastname
# #         self.idnumber = idnumber
# #     def display(self):
# #         print(f"name is {self.firstname + self.lastname} and id is {self.idnumber}")
# # class Student(Person):
# #     def __init__(self,firstname,lastname,idnumber,marks):
# #         super().__init__(firstname,lastname,idnumber)
# #         self.marks = marks
# #     def calculate(self):
# #         avg = sum(self.marks) / len(self.marks)
# #         if avg >= 90:
# #             return 'O'  # Outstanding
# #         elif avg >= 80:
# #             return 'E'  # Exceeds Expectations
# #         elif avg >= 70:
# #             return 'A'  # Acceptable
# #         elif avg >= 55:
# #             return 'P'  # Poor
# #         elif avg >= 40:
# #             return 'D'  # Dreadful
# #         else:
# #             return 'T'  # Troll
        
# # s1 = Student("kanaka","chaithu", 35 , [12,13,14,15])
# # s1.calculate()
# # print(f"Grade: {s1.calculate()}")


# # class Book:
# #     def __init__(self,title,pages):
# #         self.title=title
# #         self.pages=pages
# #     def __add__(self, other,next):
# #         total=self.pages+other.pages
# #         return total
# # b1=Book('One indian girl', 300)
# # b2=Book('making india awesome',200)
# # b3=Book('half girlfriend', 400)
# # print("total number of pages", b1+b2+b3)


# # class Vehicle:
   
# #     def __init__(self, name, max_speed, mileage, color = 'white'):
# #         self.name = name
# #         self.max_speed = max_speed
# #         self.mileage = mileage
# #         self.color = color

# # class Bus(Vehicle):
# #     pass

# # class Car(Vehicle):
# #     pass

# # b1=Bus('ai', 120, 2000)
# # print(b1.__dict__)



# # n = int(input("enter number:"))
# # power = len(str(n))
# # temp = n
# # arm = 0
# # while temp > 0:
# #     rem = temp % 10
# #     arm = arm + (rem**power)
# #     temp = temp//10
# # if  n == arm:
# #     print("is arm")
# # else :
# #     print("not not arm")          

# # import numpy as np
# # array = np.random.randint(0,25,10)
# # max = np.max(array)
# # index = array.argmax()
# # print(array)
# # print(max)
# # print(index)
# # # shape = (array.reshape(2,5))
# # # print(shape)

# # import numpy as np
# # array = np.arange(1,11)
# # slice_of_array = array[0:6

# # print(slice_of_array)
# # print(array)

# # import numpy_test as np
# # array = np.arange(50).reshape(5,10)
# # # print(array)
# # sub=(array[1:4])
# # # print(sub)
# # sub2 = sub[0:,1:4]
# # print(sub2)

# # from abc import ABC, abstractmethod

# # class Weapon(ABC):
    
# #     def equip(self):
# #         print("Weapon equipped 🎯")

# #     @abstractmethod
# #     def attack(self):
# #         pass


# # class Sword(Weapon):
# #     def attack(self):
# #         print("Swinging sword ⚔️")

# # class Gun(Weapon):
# #     def attack(self):
# #         print("Firing gun 🔫")

# # # Try it
# # player_weapon = Gun()
# # player_weapon.equip()
# # player_weapon.attack()



# def log_function_call(func):
#     def wrapper(*args,**kwargs):
#         print(f"function is:{func.__name__}")
#         print(f"arguments:{args}")
#         result = func(*args,**kwargs)
#         print(result)
#         return result
#     return wrapper
# @log_function_call
# def Multiply(a,b):
#     return a * b
# def Add(a,b):
#     return a + b
# Multiply(3,4)

# # from abc import ABC,abstractmethod
# # class Shape(ABC):
# #     @abstractmethod
# #     def area(self):
# #         pass
# # class Rectangle_area(Shape):
# #     def __init__(self,length,bredth):
# #         self.length = length
# #         self.bredth = bredth
# #     def area(self):
# #         return self.length * self.bredth
# #         print(area)
# # rectangle = Rectangle_area(10,20)
# # print(rectangle.area())

        
# # from abc import ABC,abstractmethod
# # class Vehicle(ABC):
# #     @abstractmethod
# #     def max_speed(self):
# #         pass
# # class bike(Vehicle):
# #     def __init__(self,brand,topspeed):
# #         self.brand = brand
# #         self.topspeed = topspeed
# #     def max_speed(self):
# #         print(f"the max speed of {self.brand} is {self.topspeed} km/h")
# # class car(Vehicle):
# #     def __init__(self,brand,topspeed):
# #         self.brand = brand
# #         self.topspeed = topspeed
# #     def max_speed(self):
# #         print(f"the max speed of {self.brand} is {self.topspeed} km/h")
# # vehicle_type = input("Enter vehicle type (car/bike): ").strip().lower()

# # b1 = bike()
# # b1.max_speed()
# # c1 = car()
# # c1.max_speed()

# # def generate_even_numbers(n):
# #     even_list = []
# #     for i in range (1,n+1):
# #         if i % 2 == 0:
# #             even_list.append(i)
# #     print(even_list)
# # gen = generate_even_numbers(10)

# # import threading
# # import time
# # import random

# # def download_file(file_name):
# #     print(f"Started downloading {file_name}")
# #     time_to_download = random.randint(1, 3)
# #     time.sleep(time_to_download)
# #     print(f"Finished downloading {file_name}")

# # # List of files
# # files = ["file1.txt", "file2.txt", "file3.txt", "file4.txt"]

# # # Create and start threads
# # threads = []

# # for file in files:
# #     thread = threading.Thread(target=download_file, args=(file,))
# #     thread.start()
# #     threads.append(thread)

# # # Wait for all threads to complete
# # for thread in threads:
# #     thread.join()

# # print("All downloads completed!")

# import numpy as np
# from flask import Flask, request, jsonify, render_template
# import joblib
# import sqlite3

# import numpy as np
# import pandas as pd
# from sklearn import metrics 
# import warnings
# import pickle
# import pandas as pd
# import numpy as np
# import pickle
# import sqlite3
# import random

# import smtplib 
# from email.message import EmailMessage
# from datetime import datetime

# warnings.filterwarnings('ignore')



# app = Flask(__name__)


# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route("/about")
# def about():
#     return render_template("about.html")


# @app.route('/home')
# def home1():
# 	return render_template('home.html')


# @app.route('/logon')
# def logon():
# 	return render_template('signup.html')

# @app.route('/login')
# def login():
# 	return render_template('signin.html')


# @app.route("/signup")
# def signup():
#     global otp, username, name, email, number, password
#     username = request.args.get('user','')
#     name = request.args.get('name','')
#     email = request.args.get('email','')
#     number = request.args.get('mobile','')
#     password = request.args.get('password','')
#     otp = random.randint(1000,5000)
#     print(otp)
#     msg = EmailMessage()
#     msg.set_content("Your OTP is : "+str(otp))
#     msg['Subject'] = 'OTP'
#     msg['From'] = "evotingotp4@gmail.com"
#     msg['To'] = email
    
    
#     s = smtplib.SMTP('smtp.gmail.com', 587)
#     s.starttls()
#     s.login("evotingotp4@gmail.com", "xowpojqyiygprhgr")
#     s.send_message(msg)
#     s.quit()
#     return render_template("val.html")

# @app.route('/predict_lo', methods=['POST'])
# def predict_lo():
#     global otp, username, name, email, number, password
#     if request.method == 'POST':
#         message = request.form['message']
#         print(message)
#         if int(message) == otp:
#             print("TRUE")
#             con = sqlite3.connect('signup.db')
#             cur = con.cursor()
#             cur.execute("insert into `info` (`user`,`email`, `password`,`mobile`,`name`) VALUES (?, ?, ?, ?, ?)",(username,email,password,number,name))
#             con.commit()
#             con.close()
#             return render_template("signin.html")
#     return render_template("signup.html")

# @app.route("/signin")
# def signin():

#     mail1 = request.args.get('user','')
#     password1 = request.args.get('password','')
#     con = sqlite3.connect('signup.db')
#     cur = con.cursor()
#     cur.execute("select `user`, `password` from info where `user` = ? AND `password` = ?",(mail1,password1,))
#     data = cur.fetchone()

#     if data == None:
#         return render_template("signin.html")    

#     elif mail1 == str(data[0]) and password1 == str(data[1]):
#         return render_template("home.html")
#     else:
#         return render_template("signin.html")

# @app.route("/notebook")
# def notebook1():
#     return render_template("Notebook.html")



# @app.route('/predict',methods=['POST'])
# def predict():
#     int_features= [float(x) for x in request.form.values()]
#     print(int_features,len(int_features))
#     final4=[np.array(int_features)]
#     model = joblib.load('model.sav')
#     predict = model.predict(final4)

#     if predict==0:
#         output='There is No Attack Detected and Its BENIGN!'
#     elif predict==1:
#         output='Attack is Detected and Its BOT ATTACK!'
#     elif predict==2:
#         output='Attack is Detected and Its BRUTEFORCE ATTACK!'
#     elif predict==3:
#         output='Attack is Detected and Its DDoS ATTACK!'
#     elif predict==4:
#         output='Attack is Detected and its DOS ATTACK!'
#     elif predict==5:
#         output='Attack is Detected and its PORTSCAN ATTACK!'
#     elif predict==6:
#         output='Attack is Detected and its WEB-ATTACK!'
    
#     return render_template('prediction.html', output=output)



# if __name__ == "__main__":
#     app.run(debug=True)



# n = 121
# temp = n
# rev = 0
# while temp > 0:
#     rem = temp % 10
#     rev = rev * 10 +rem
#     temp = temp//10
# if n == rev:
#     print("is a palindrome")
# else:
#     print("not a palindrome")




# n = int(input("enter an number"))
# p = len(str(n))
# arm = 0
# temp = n
# while temp > 0:
#     rem = temp%10
#     arm = arm + rem ** p
#     temp = temp//10
# print(arm)
# if (n ==arm ):
#     print("is a armstrong number")
# else:
#     print("not")

# n = 121
# temp = n
# rev = 0
# while temp > 0:
#     rem = temp % 10
#     rev = rev*10 + rem
#     temp = temp // 10
# print(rev)


# def factorial(num):
#     fact = 1
#     for i in range (1,num+1):
#         fact = fact * i
#     return(fact)
# num = 6
# a = factorial(num)
# print(a)


# n = 5
# for i in range(2,n):
#     if n % i == 0:
#         print("not a prime")
#         break
#     else :
#         print("is a prime")
#         break

# n = 6
# prime = []
# for i in range (2,n+1):
#     for j in range (2, i):
#         if i % j == 0:
#             break
#     else:
#             prime.append(i)
# print(prime)

# n = int(input("Enter how many prime numbers you want: "))
# prime_count = 0   # count of primes found
# num = 2           # number to check

# while prime_count < n:
#     # check if num is prime
#     for j in range(2, int(num**0.5)+1):
#         if num % j == 0:
#             break
#     else:
#         print(num, end=" ")
#         prime_count += 1
#     num += 1



