# =======================================================================================
print("===== Quiz Game =====")
# =======================================================================================

name = input("Enter Name :")
age = int(input("Enter Age :"))

print(f"""
Player Name : {name}
Age : {age}
      """)

# =======================================================================================

ques1 = "Capital of India?"
print(ques1)

answer1 = input("Enter Answer No- 1 :")
print(answer1)

# =======================================================================================
score = 0

if answer1 == "delhi":
    score = score + 1
    print("Correct Answer ")
    print("Score =", score)

else:
    print("Wrong Answer")

# =======================================================================================

ques2 = " 2 + 2 = ?"
print(ques2)

answer2 = int(input("Enter Answer No- 2 :"))
print(answer2)

# =======================================================================================

if answer2 == 4:
    score = score + 1
    print("Correct Answer")
    print("Score =", score)

print("\n")
if score == 2:
    result = "Pass"
else:
    result = "Fail"

print("Result =", result)

# =======================================================================================
# Dictionary-
# =======================================================================================

quiz = {"Player Name": name, "Age": age, "Total Score": score, "Result": result}

print(quiz)

# =======================================================================================

print("\n ===== Quiz Game ===== ")
print("Player Name :", quiz["Player Name"])
print("Total Score :", quiz["Total Score"])
print("Result :", quiz["Result"])

# =======================================================================================
