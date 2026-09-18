# Empty Dictionary-
# ======================================================================================
"""Write a program to enter marks of 3 subjects from the user
 and store them in a dictionary.
Start with an empty dictionay & add one by one.
Use subject name as key & marks as value."""
# ======================================================================================

marks = {}  # Empty Dictionary.

x = int(input("Enter Maths Marks: "))
marks.update({"Maths": x})

y = int(input("Enter Physics Marks: "))
marks.update({"Physics": y})

z = int(input("Enter Chemistry Marks: "))
marks.update({"Chemistry": z})

print(marks)
print(type(marks))

# ======================================================================================