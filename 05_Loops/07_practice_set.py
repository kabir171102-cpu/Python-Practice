# Let's Practice-
# =======================================================================================
# Ques 1- Count vowels in a string.
# =======================================================================================

text = input("Enter Text :")  #  Python Programming
count = 0

for i in text:
    if i in "aeiouAEIOU":
        count += 1

print("Total Vowels =", count)

# =======================================================================================
# Ques 2- Reverse a string.
# =======================================================================================

user_input = input("Enter Input :")
reverse_text = ""

for i in user_input:
    reverse_text = i + reverse_text

print(reverse_text)

# =======================================================================================
# Ques 3- Print all prime numbers between 1 and 50.
# =======================================================================================

for num in range(2, 51):
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)

# =======================================================================================
# Ques 4- Count how many prime numbers are present between 1 and 100.
# =======================================================================================

count = 0

for num in range(2, 101):
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num)
        count += 1
print("Total =", count)

# =======================================================================================
# Ques 5- Print in this Pattern.
# =======================================================================================

for i in range(1, 6):
    for j in range(i):
        print("*", end="")

    print()

# =======================================================================================
# Ques 6- Print in this Pattern.
# =======================================================================================

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")

    print()

# =======================================================================================
# Ques 7- Print in this Pattern.
# =======================================================================================

for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")

    print()

# =======================================================================================
# Ques 8- Print in this Pattern.
# =======================================================================================

for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")

    print()

# =======================================================================================
# Ques 9- Print in this Pattern.
# =======================================================================================

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")

    print()

# =======================================================================================
# Ques 10- 1 se 100 tak jitne numbers 3 aur 5 dono se divisible hain,
#          unka count aur sum print karo.
# =======================================================================================

total = 0
count = 0

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)
        count += 1
        total += i

print("Count =", count)
print("Total =", total)

# =======================================================================================
