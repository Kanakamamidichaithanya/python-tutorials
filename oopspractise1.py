# class student:
#     name = "chaithanya"
# s1=student()
# print(s1.name)


# class student:
#     def __init__(self,name,surname):
#         self.name = name
#         self.surname = surname
#         print("adding new studemt into the database")

# s1 = student("chaithanya","kanakamamidi")
# print(s1.name, s1.surname)



# class cars :
#     def __init__ (self,model,build):
#         self.model = model
#         self.build = build
# c1 = cars("toyota" , "fortuner")
# print(c1.build, c1.model)        


# class cars:
#     def __init__(self,name,company):
#         self.name = name
#         self.company = company
#         print(self.name ,self.company)
#     def enter(self):
#         print(f"welcome to {self.company} community")
#     def price(self,price):
#         self.price = price
#         print("the price of the car is:",self.price)    

# c1 = cars("fortuner","toyota")
# c1.enter()
# c1.price(300000)

  


# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#     def avg(self):
#         sum = 0
#         for i in self.marks:
#             sum += i                     #program for taking student details and finding average subjects
#         print(sum/3)

# name = input("Enter the student's name: ")
# marks = input("Enter the student's marks (separated by spaces): ")
# marks = list(map(int,marks.split()))
# S1 = Student(name, marks)
# S1.avg()



# class Account:
#     def __init__(self,accnumber,balance):
#         self.account_no = accnumber
#         self.balance = balance
#         print(accnumber,balance)
#     def creditamount(self,amount):
#         self.credited_amnt = amount
#         total_amount = self.credited_amnt + self.balance
#         print("your total amount:", total_amount )
#     def debitamount(self,amount):
#         self.debited_amnt = amount
#         total_amount = self.balance - self.debited_amnt 
#         print("your total amount:", total_amount )
#     def getbalance(self):
#         return self.balance

# account1 = Account(1234,100000)
# account1.creditamount(10000)
# account1.debitamount(20000)

# account2 = Account(3456,15000)
# account2.creditamount(30000)
# account2.debitamount(5000)



# class Dog:
#     def __init__(self, name, breed):
#         self.name = name  # Attribute
#         self.breed = breed  # Attribute

#     def bark(self):  # Method
#         print(f"{self.name} says woof!")

# # Creating an object (instance) of the Dog class
# my_dog = Dog("Buddy", "Golden Retriever")
# my_dog.bark()


    
      



