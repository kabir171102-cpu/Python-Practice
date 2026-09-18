# # ==========================================================================================
# # Question 1- Write a python program that will sum numbers present in given list of data.

# # excepted output:-
# # enter the list:- [1, "a", "b", 3]
# # ==========================================================================================

# def sum_of_int_list(my_list):
#     total = 0
#     for element in my_list:
#         try:
#             int(element)
#         except:
#             print(f"item {element} is not a number")
#         else:
#             total += element

#     return total
    
# print(sum_of_int_list([1, "a", "b", 3]))

# "Output"
# # item a is not a number
# # item b is not a number
# # 4

# ==========================================================================================
# Question 2- Find the error and fix it.
def total_likes():
    reviews = [{"Image": 3, "like": 20, "Comment": 10},
               {"like": 15, "Comment": 8, "Share" : 10},
               {"Image": 7, "Comment": 16, "Share" : 37},
               {"Image": 6, "like": 10, "Comment" : 9}]

    total = 0
    for review in reviews:
        try:
            total += review["like"]
        except:
            pass
    return total

print(total_likes())   # 45
