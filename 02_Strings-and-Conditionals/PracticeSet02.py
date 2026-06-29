"""Let's Practice"""

# ========================================================================================
# Question 1- Write a program to check if a number entered by the user is Odd or Even.
# ========================================================================================

num = int(input("Enter the Number: "))

if num % 2 == 0:  # (% gives remainder.)
    print("Even")
else:
    print("Odd")

# =====
# Or
# =====

num = int(input("Enter the Number: "))

remain = num % 2

if remain == 0:
    print("Even")
else:
    print("Odd")

# =========================================================================================
