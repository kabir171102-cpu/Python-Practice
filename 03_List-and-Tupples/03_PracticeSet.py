# """Let's Practice"""

# =====================================================================================
# Question 1- Write a program to ask the user to enter names of
# their 3 favorite movies and store them in a list.
# =====================================================================================

# (a)

movie1 = input("Enter First Movie Name :")
movie2 = input("Enter Second Movie Name :")
movie3 = input("Enter Third Movie Name :")
movies = [movie1, movie2, movie3]
print(type(movies))  # <class 'list'>
print(movies)  # Lucky The Racer, Yevadu Return, Son of Satyamurti.

# =====
# Or- (b)
# =====
# """We can also use .append formula"""
# ======================================================================================

movies = []
mov1 = input("Enter 1st movie :")
mov2 = input("Enter 2nd movie :")
mov3 = input("Enter 3rd movie :")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(type(movies))
print(movies)

# ========
# Or- (c)
# ========

movies = []
mov = input("Enter 1st movie :")
movies.append(mov)
mov = input("Enter 2nd movie :")
movies.append(mov)
mov = input("Enter 3rd movie :")
movies.append(mov)

print(movies)
print(type(movies))

# =======================================================================================
# Question 2- Write a program to check if a list contains a palindrome of elements.
#             (Hint: use copy() method).
#             [1, 2, 3, 2, 1]                     [1, "abc", "abc", 1]
# =======================================================================================

list1 = [1, 2, 1]

copy_list1 = list1.copy()
copy_list1.reverse()

if copy_list1 == list1:
    print("Palindrome")
else:
    print("Not Palindrome")  # Palindrome

# ======================================================================================

list2 = [1, 2, 3]

copy_list2 = list2.copy()
copy_list2.reverse()

if copy_list2 == list2:
    print("Palindrome")
else:
    print("Not Palindrome")  # Not Palindrome

# ======================================================================================
# Question 3- Alphabet Check
# ======================================================================================


list1 = ["a", "b", "c", "b", "a"]
list2 = ["a", "b", "c", "a", "b", "c", "d"]

# ==========================================

# List1-
copy_list1 = list1.copy()
copy_list1.reverse()

if copy_list1 == list1:
    print("Palindrome")
else:
    print("Not Palindrome")  # Palindrome.

# =====================================================================================
# List2-
copy_list2 = list2.copy()
copy_list2.reverse()

if copy_list2 == list2:
    print("Plindrome")
else:
    print("Not Palindrome")  # Not Palindrome.

# =====================================================================================
