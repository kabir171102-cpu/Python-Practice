# Let's Start-
# ================================================================================
# Question 1- Print numbers from 1 to 10 using recursion.
# ================================================================================

def show(n):
    if n == 11:
        return
    print(n)
    show(n + 1)

show(1)

# ================================================================================
# Question 2- Print numbers from 10 to 1 using recursion.
# ================================================================================

def show(n):
    if n == 0:
        return
    print(n)
    show(n - 1)

show(10)

# ================================================================================
# Question 3- Find the sum of numbers from 1 to n using recursion.
# ================================================================================
n = int(input("Enter Number: "))

def find_sum(n):
    if n == 0:
        return 0
    return find_sum(n - 1) + n

total = find_sum(n)
print("Total Sum =",total)

# ==================================================================================
# Question 4- Find the factorial of a number using recursion.
# ==================================================================================

def find_fact(num):
    fact = 1
    if num == 1:
        return 1
    for i in range(1, num + 1):
        fact *= i
    return "Factorial of",num,"=",fact

num = int(input("Enter Number: "))
print(find_fact(num))
    
# ==================================================================================
# Question 5- Find the nth Fibonacci number using recursion.
# ==================================================================================

def fib(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    return fib(num - 1) + fib(num - 2)

num = int(input("Enter Number: "))
print(fib(num))

# ==================================================================================
# Question 6- Reverse a string using recursion.
# ==================================================================================
