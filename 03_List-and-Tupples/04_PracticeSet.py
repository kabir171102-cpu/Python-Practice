# ===========================================================================================
# Question 1- Write a program to count the number of students
#             with the "A" grade in the following tuple"""
#                       ["C", "D", "A", "A", "B", "B", "A"]
# ===========================================================================================

grade = ("C", "D", "A", "A", "B", "B", "A")  # Tuple.
print(grade.count("A"))  # 3
print(type(grade))

# ===========================================================================================
# Question 2- Store the above values in a list & sort them from "A" to "D" .
# ===========================================================================================

grade = ["C", "D", "A", "A", "B", "B", "A"]
grade.sort()  # Ascending order
print(grade)
print(type(grade))  # <class 'list'>

# ===========================================================================================
