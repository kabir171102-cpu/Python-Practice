# =========================================================================================
# Print Biggest of 2 Number
# =========================================================================================

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

if a > b:
    print("Biggest number is", a)
else:
    print("Biggest number is", b)

# If we enter both numbers same then (else) will always print.

# =========================================================================================
# Prnit Biggest/Smallest of 3 Number
# =========================================================================================

# Biggest
# =========
a = int(input("First Number: "))
b = int(input("Second Number: "))
c = int(input("Third Number: "))

if a >= b and a >= c:
    biggest = a
elif b >= a and b >= c:
    biggest = b
else:
    biggest = c

# ==========================================================================================

# Smallest
# =========

if a <= b and a <= c:
    smallest = a
elif b <= a and b <= c:
    smallest = b
else:
    smallest = c

print("Biggest number is", biggest)
print("Smallest number is", smallest)

# ==========================================================================================
# Method 2.
# ==========================================================================================

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print("Biggest:", max(a, b, c))
print("Smallest:", min(a, b, c))

# ===========================================================================================
