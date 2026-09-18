# =========================================================================================
# Question 1- Write a program to user's first name & print its length
# =========================================================================================

name = "Krishna"
print(len(name))  # 7.
# or
name = input("Enter your name: ")
print("Length of name =", len(name))

# ==========================================================================================
# Question 2- Write a program to find the occurrence of '$' in a string.
# ek string me $ kitni baar aata hai uski occurrences nikalna hai.
# ==========================================================================================

string = "In $ummer holiday$ we will go to watch the $tranger thing$."
print(string.count("$"), "Times")  # printed  4 times.

# ==========================================================================================
