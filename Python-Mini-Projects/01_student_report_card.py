# =======================================================================================
print("==== Student Report Card ====")
# =======================================================================================

# =================
# Student Info-
# =================

# =======================================================================================
name = input("Enter Name :")
father_name = input("Enter Father Name :")
Class = input("Enter Class :")
roll_no = int(input("Enter Roll no :"))
age = int(input("Enter Age :"))
gender = input("Enter Sex :")


print(f"""
Name : {name}
Father Name : {father_name}
Class : {Class}
Roll No : {roll_no}
Age : {age}
Gender : {gender}
""")
# =======================================================================================

# =================
# Marks-
# =================

# =======================================================================================
maths = float(input("Enter Maths Marks :"))
phys = float(input("Enter Physics Marks :"))
chem = float(input("Enter Chemistry Marks :"))
hindi = float(input("Enter Hindi Marks :"))
english = float(input("Enter English Marks :"))

print(f"""
Maths : {maths}
Physics : {phys}
Chemistry : {chem}
Hindi : {hindi}
English : {english}
      """)
# =======================================================================================

# =================
# Percentage-
# =================

# =======================================================================================
total = maths + phys + chem + hindi + english

percentage = total / 5

print(percentage)
# =======================================================================================

# =================
# Result-
# =================

# =======================================================================================
if (
    maths >= 33
    and phys >= 33
    and chem >= 33
    and hindi >= 33
    and english >= 33
    and percentage >= 40
):
    result = "Pass"
else:
    result = "Fail"

print(result)
# =======================================================================================

# =================
# Grade-
# =================

# =======================================================================================
if percentage >= 80:
    grade = "A"
elif percentage >= 60 and percentage < 80:
    grade = "B"
elif percentage >= 50 and percentage < 60:
    grade = "C"
else:
    grade = "D"
# =======================================================================================

# =================
# Division-
# =================

# =======================================================================================
if grade == "A":
    division = "1st"
elif grade == "B":
    division = "B"
elif grade == "C":
    division = "C"
else:
    division = "D"

print(division)
# =======================================================================================

# =================
# Dictionary-
# =================

# =======================================================================================
student = {
    "Name": name,
    "Father Name": father_name,
    "Class": Class,
    "Roll No": roll_no,
    "Age": age,
    "Gender": gender,
    "Maths Mark": maths,
    "Physics Mark": phys,
    "Chemistry Mark": chem,
    "Hindi Mark": hindi,
    "English Mark": english,
    "Percentage": percentage,
    "Result": result,
    "Grade": grade,
    "Division": division,
}
# =======================================================================================


# =======================================================================================

print("\n ==== Report Card ====")
print("Name :", student["Name"])
print("Father Name :", student["Father Name"])
print("Class :", student["Class"])
print("Roll No :", student["Roll No"])
print("Age :", student["Age"])
print("Gender :", student["Gender"])
print("Maths Mark :", student["Maths Mark"])
print("Physics Mark :", student["Maths Mark"])
print("Chemistry Mark :", student["Chemistry Mark"])
print("Hindi Mark:", student["Hindi Mark"])
print("English Mark :", student["English Mark"])
print("Percentage :", student["Percentage"])
print("Result :", student["Result"])
print("Grade", student["Grade"])
print("Division :", student["Division"])

# =======================================================================================
