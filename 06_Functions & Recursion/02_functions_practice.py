# Let's Start-
# ============================================================================
# Question 1- Create a function that prints "Hello, Python!"
# ============================================================================

def print_hello():
    print("Hello, Python!")

print_hello()

# ============================================================================
# Question 2- Create a function that takes a number as a parameter
#  and prints its square.
# ============================================================================

def print_square(num):
    print(num ** 2)

print_square(5)

# ============================================================================
# Question 3- Create a function that takes two numbers and prints their sum.
# ============================================================================

def print_sum(a, b):
    print(a + b)
    return

print_sum(2, 5)

# ==============================================================================
# Question 4- Create a function that checks whether a number is even or odd.
# ==============================================================================

def check_condition(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

num = int(input("Enter Number: "))
check_condition(num)

# ==============================================================================
# Question 5- Create a function that returns the largest of two numbers.
# ==============================================================================

def return_largest(a, b):
    if a > b:
        return a,"is Largest"
    else:
        return a,"is Largest"

print(return_largest(10, 12))

# ==============================================================================
# Question 6- Create a function that returns the factorial of a number.
# ==============================================================================

def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return "Factorial of",num, "=",fact

num = int(input("Enter Number: "))
print(factorial(num))

# ==============================================================================
# Question 7- Create a function that counts the vowels in a string.
# ==============================================================================


def check_vowels():
    count = 0
    string = "AmanKabirAbhayRajKrishnaKishuAbhishekKuldeep"

    for i in string:
        if i in "aeiouAEIOU":
            count += 1
    print("Total =",count)

check_vowels()

# ==============================================================================
# Question 8- Create a function that checks whether a string is a palindrome.
# ==============================================================================

def check_palin(text):
    if text  ==  text[::-1]:
        return "Palindrime"
    else:
        return "Not Palindrome"

string = input("Enter String: ")
print(check_palin(string))

# ================================================================================
# Question  9- Create a function that returns the sum of all elements in a list.
# ================================================================================

def print_sum(sum):
    total = 0
    for i in sum:
        total +=  i
    return "Total =",total

sum = [2, 3, 4, 5, 8]
print(print_sum(sum))

# ==================================================================================
# Question 10- Create a function that checks whether a given number is prime.
# ==================================================================================

def is_prime(num):
    if num <= 1:
        return "Not Prime"
    
    for i in range(2, num):
        if num % i == 0:
            return "Not Prime"
        
    return "Prime"

num = int(input("Enter Number: "))
print(is_prime(num))

