# Let's Practice-
# =======================================================================================
# Question 1- Print all odd numbers from 1 to 100,
#             and count how many odd numbers were printed.
# =======================================================================================

count = 0

for i in range(1, 101):
    if i % 2 != 0:
        print(i)
        count += 1
print("Total Odd Numbers =", count)

# =======================================================================================
# Question 2- Calculate the sum of all numbers from 1 to 100
# =======================================================================================

sum = 0
for i in range(1, 101):
    sum = sum + i
print("Total Sum =", sum)

# =======================================================================================
# Question 3- Calculate the factorial of a number entered by the user
# =======================================================================================

num = int(input("Enter Number :"))
factorial = 1
i = 1

while i <= num:
    factorial *= i
    i += 1
print("Factorial =", factorial)

# =======================================================================================
# Question 4- Print all numbers from 1 to 50,
#             that are divisible by 3 but not divisible by 2.
# =======================================================================================

for i in range(1, 51):
    if i % 3 == 0 and i % 2 != 0:
        print(i)

# =======================================================================================
# Question 5- Count how many vowels are present in a string entered by the user
# =======================================================================================

text = input("Enter Text :")
count = 0


for i in text:

    if i in "aeiouAEIOU":
        count += 1

print("Total Vowels =", count)

# =======================================================================================
# Question 6- Count how many digits are present in a string entered by the user.
# =======================================================================================

user_input = input("Enter Str :")
count = 0

for i in user_input:
    if i in "0123456789":
        count += 1

print("Total Digit =", count)

# =======================================================================================
# Question 7- Count how many uppercase letters are present in a string
#             entered by the user.
# =======================================================================================

text = input("Enter Text :")  # PyThOn123

count = 0
for i in text:
    if i.isupper():
        count += 1

print("Total Uppercase Alphabet =", count)

# =======================================================================================
# Question 8- Count how many lowercase letters, uppercase letters, digits,
#             and special characters are present in a string
# =======================================================================================

text = input("Enter Text :")  # PyThOn@123

upper = 0
lower = 0
digit = 0
special = 0

for i in text:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1
    elif i.isdigit():
        digit += 1
    else:
        special += 1

print(f"""
      Upper Case : {upper}
      Lower Case : {lower}
      Digit : {digit}
      Special Character : {special}
      """)

# =======================================================================================
