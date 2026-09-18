# ==========================================================================================
# Question 1- Write a program to find the greatest of 3 numbers entered by the user.
# ==========================================================================================

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))

if a > b and a > c:
    print("First Number is Largest =", a)
elif b > a and b > c:
    print("Second Number is Largest =", b)
else:
    print("Third Number is Largest =", c)

# ==========================================================================================
