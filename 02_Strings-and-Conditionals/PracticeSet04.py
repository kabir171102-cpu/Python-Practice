# ==========================================================================================
# Question 1- Write a program to check if a number is a multiple of 7 or not.
# ==========================================================================================


num = int(input("Enter the Number: "))

if num % 7 == 0:
    print(num, "is a multiple of 7")
else:
    print(num, "is not a multiple of 7")

# =======
# Or-
# =======

num = int(input("Enter Number: "))

remain = num % 7
if remain == 0:
    print(num, "is a multiple of 7")
else:
    print(num, "is not a multipe of 7")

# ===========================================================================================
