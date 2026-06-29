# ========================================================================================
# Question 1- Print the sum(+), difference(-), prouct(*), Quoteint(/)

# | Word       | Meaning        | Symbol |
# | ---------- | -------------- | ------ |
# | Sum        | Addition       | +      |
# | Difference | Subtraction    | -      |
# | Product    | Multiplication | *      |
# | Quotient   | Division       | /      |

a = 15
b = 5
print(a + b)
print(a - b)
print(a * b)
print(a / b)

# ========================================================================================
# Question 2- Swap 2 variables
# ========================================================================================

a = 5
b = 10

a, b = b, a
print("a =", a)
print("b =", b)

# =======
# Or-
# METHOD 2 (Using Third Variable).
# =======

a = 5
b = 10

temp = a
a = b
b = temp

print("a =", a)
print("b =", b)
# =======
# Or-
# METHOD 3 (Without Third Variable (Advanced).
# =======

a = 5
b = 10

a = a + b
b = a - b
a = a - b

print("a =", a)
print("b =", b)

# ======================================================================================
# Question 3- Simple Interest
# ======================================================================================

p = float(input("Principal: "))
r = float(input("Rate: "))
t = float(input("Time: "))

si = (p * r * t) / 100
print(si)

# ======================================================================================
# Question 4- Temprature Convertor
# ======================================================================================

c = float(input("Celsius: "))

f = 9 / 5 * c + 32
print(f, "K")

# ======================================================================================
