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


