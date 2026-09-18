# # Let's Practice-
# # =======================================================================================
# # Question 1- Create a class Student with attributes name and age.
# #             Create one object and print both values.
# # =======================================================================================

# class Student:
#     name = "Kabir"
#     age = 21

# s1 = Student()
# print(s1.name)
# print(s1.age)

# # =======================================================================================
# # Question 2- Create a class Car with attributes brand and model. Print the details.
# # =======================================================================================

# class Car:
#     brand = "Toyota"
#     model = "Fortuner"

# car1 = Car()
# print(car1.brand)
# print(car1.model)

# # =======================================================================================
# # Question 3- Create two objects of the same class with different data.
# # =======================================================================================

# class Student:
#     pass

# s1 = Student()
# s1.name = "Aman"

# s2 = Student()
# s2.name = "Kabir"

# print(s1.name)
# print(s2.name)

# # =======================================================================================
# # Question 4- Create a Student class using __init__() to initialize name and age.
# # =======================================================================================

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# s1 = Student("Kabir", 21)
# print("Student Name:",s1.name)
# print("Age: ",s1.age)

# # =======================================================================================
# # Question 5- Create a Laptop class with brand, ram, and price.
# # =======================================================================================

# class Laptop:
#     def __init__(self, brand, ram, price):
#         self.brand = brand
#         self.ram = ram
#         self.price = price

# lapt = Laptop("Dell", "8GB", 40000)
# print("Laptop Brand:",lapt.brand)
# print("RAM:",lapt.ram)
# print("Price:",lapt.price)

# # =======================================================================================
# # Question 6- Create three Employee objects using a constructor.
# # =======================================================================================

# class Employee:
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary

# e1 = Employee("Aman", 21, 15000)
# print("Employee1 Name:",e1.name)
# print("Age:",e1.age)
# print("Salary:",e1.salary)

# print()

# e2 = Employee("Abhay", 23, 40000)
# print("Employee2 Name:",e2.name)
# print("Age:",e2.age)
# print("Salary:",e2.salary)

# print()

# e3 = Employee("Krishna", 24, 35000)
# print("Employee3 Name:",e3.name)
# print("Age:",e3.age)
# print("Salary:",e3.salary)

# # =======================================================================================
# # Question 7- Create a method display() that prints students details.
# # =======================================================================================

# class Student:
#     def __init__(self, name, age, roll_no):
#         self.name = name
#         self.age = age
#         self.roll_no = roll_no

#     def display(self):
#         print("Student Name:",self.name)
#         print("Age:",self.age)
#         print("Roll No:",self.roll_no)


# s1 = Student("Aman Yadav", 21, 13)
# s1.display()

# print()

# s2 = Student("Abhay Kumar", 23, 3)
# s2.display()

# print()

# s3 = Student("Krishna Gond", 24, 7)
# s3.display()

# # ==========================================================================================
# # Question 8- Create a method is_adult() that prints "Adult" if age ≥ 18, otherwise "Minor".
# # ==========================================================================================

# class Age_check():
#     def __init__(self, age):
#         self.age = age

#     def is_adult(self):
#         if self.age >= 18:
#             print("Adult")
#         else:
#             print("Minor")

# adult_check = Age_check(21)
# adult_check.is_adult()

# # ==========================================================================================
# # Question 9- Create a Rectangle class with length and width.
# #             Create a method to calculate area.
# # ==========================================================================================

# class Rectangle():
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         print("Area =",self.length * self.width,"cm")

# area_calculate = Rectangle(13, 16)
# area_calculate.area()

# # ==========================================================================================
# # Question 10- Create a class variable school = "ABC Public School" 
# #              and print it using two objects.
# # ==========================================================================================

# class Student:
#     school = "ADM Public School"

# s1 = Student()
# s2 = Student()

# print(s1.school)
# print(s2.school)

# # ============================================================================================
# # Question 11- Count how many objects have been created.
# # ============================================================================================

# class Student:
#     count = 0

#     def __init__(self, name):
#         self.name = name
#         Student.count += 1

# s1 = Student("Aman Yadav")
# print(s1.name)

# s2 = Student("Abhay Kumar")
# print(s2.name)

# s3 = Student("Krishna Gond")
# print(s3.name)

# s4 = Student("Abhishek Das")
# print(s4.name)

# print("Total Student =",Student.count)

# # ============================================================================================
# # Question 12- Create a class BankAccount with balance.
# #              Create methods deposit() and withdraw().
# # ============================================================================================

# class BankAccount:

#     def __init__(self, balance):
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance = self.balance + amount

#     def withdraw(self, amount):
#         self.balance = self.balance - amount


# acc = BankAccount(1000)

# acc.deposit(500)
# acc.withdraw(200)

# print(acc.balance)



# # ============================================================================================
# # Question 13- English: Prevent negative balance while withdrawing.
# #                Hindi: Agar balance kam ho to "Insufficient Balance" print karo.
# # ============================================================================================

# class BankAccount:

#     def __init__(self, balance):
#         self.balance = balance

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient Balance")
#         else:
#             self.balance -= amount
#             print("Withdraw Successful")


# acc = BankAccount(10000)

# acc.withdraw(2000)

# print("Remaining Balance =",acc.balance)

# "Or"

# class BankAccount:

#     def __init__(self, balance):
#         self.balance = balance

#     def withdraw(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#             print("Withdraw Successful")
#         else:
#             print("Insufficient Balance")

# acc = BankAccount(1000)

# acc.withdraw(2000)

# print("Remaining Balance =",acc.balance)

# ============================================================================================
# Question 14- Create a Person class and a Student class that inherits from it.
# ============================================================================================



# ============================================================================================
# Question 15- Create a Vehicle class. Inherit Car and Bike from it.
#              Each class should have its own display() method.
# ============================================================================================