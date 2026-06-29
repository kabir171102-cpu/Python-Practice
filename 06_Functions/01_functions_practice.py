# Let's Practice-
# =======================================================================================
# Ques 1- Write a Function to print the length of a list.(list is the parameter).
# =======================================================================================

nums = [2, 3, 4, 5, 6, 7, 8]
heroes = ["Ironman", "Thor", "Captain America", "Hulk", "Dr.Strange"]
print(type(nums))


def print_len(nums):
    print(len(nums))


print_len(nums)
print_len(heroes)

# =======================================================================================
# Ques 2- Write a Function to print the elements of a list in a single line.
# =======================================================================================

villains = ["Thanos", "Ragnarok", "Homelander", "Dr.Doom"]

print(villains[0], end=" ")
print(villains[1], end=" ")


def print_villains(villains):
    for item in villains:
        print(item, end=" ")


print_villains(villains)

# =======================================================================================
# Ques 3- Write a Function to find the factorial of n.(n is the parameter).
# =======================================================================================


def cal_fact(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print("Factorial =", fact)


cal_fact(5)

# =======================================================================================
# Ques 4- Write a Function to convert USD to INR.
# =======================================================================================


def converter(usd_value):
    inr_value = usd_value * 94.5
    print(usd_value, "USD =", inr_value, "INR")


converter(10)

# =======================================================================================
# Ques 5- Check Even/Odd.
# =======================================================================================

num = int(input("Enter Number :"))


def condi_check(even_odd):
    if num % 2 == 0:
        print("Even")
    elif num % 2 != 0:
        print("Odd")


condi_check(num)

# =======================================================================================
