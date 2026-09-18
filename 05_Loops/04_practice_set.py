# Let's Practice-
# =======================================================================================
# Question 1- Print the multiplication tables from 1 to 5.
# =======================================================================================

for i in range(1, 6):
    for j in range(1, 11):
        print(i, "x", j, "=", i * j)

    print()

# =======================================================================================
# Question 2- Print the multiplication tables from 2 to 10, but only up to 5 multiples.
# =======================================================================================

for i in range(2, 11):
    for j in range(1, 6):
        print(f"{i} x {j} = {i * j}")

    print()

# =======================================================================================
# Question 3- Print all even numbers from 1 to 50,
#             and also count how many even numbers were printed.
# =======================================================================================

count = 0
for i in range(1, 51):
    if i % 2 == 0:
        print(i)
        count += 1

print("Total Even Numbers =", count)

# =======================================================================================
# Question 4- Print numbers from 1 to 100.
"""If a number is divisible by 3, print "Fizz".
If a number is divisible by 5, print "Buzz".
If a number is divisible by both 3 and 5, print "FizzBuzz".
Otherwise, print the number"""
# =======================================================================================

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# =======================================================================================
# Question 5- Print all numbers from 1 to 100 that are divisible by both 5 and 7.
#  Also print the total count of such numbers.
# =======================================================================================

count = 0
for i in range(1, 101):
    if i % 5 == 0 and i % 7 == 0:
        print(i)
        count += 1

print("Total Divisible Numbers =", count)

# =======================================================================================
# Question 6- Find the largest number in the list without using max().
# =======================================================================================

numbers = [12, 45, 7, 89, 23, 67]
largest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i
print("Largest Number =", largest)

# =======================================================================================
