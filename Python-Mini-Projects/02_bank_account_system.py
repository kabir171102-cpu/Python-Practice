# =======================================================================================
print("==== ATM System ====")
# =======================================================================================

name = input("Enter Your Name :")
age = int(input("Enter Your Age :"))
sex = input("Enter Your Sex :")
add = input("Enter Your Address :")
bank_name = input("Enter The Bank Name :")
branch_name = input("Enter The Branch Name :")
account_number = int(input("Enter The A/c Number :"))
balance = float(input("Enter The Balance :"))

print(f"""
Name : {name}
Age : {age}
Sex : {sex}
Address : {add}
Bank Name : {bank_name}
Branch Name : {branch_name}
Account Number : {account_number}
Balance : {balance}
      """)

# =======================================================================================
print("1. check balance")
print("2. deposit")
print("3. withdraw")
# =======================================================================================

choice = int(input("Choice = :"))

if choice == 1:
    print("Current balance =", balance)
elif choice == 2:

    deposit = float(input("Enter Deposit Amount :"))

    balance = balance + deposit

    print("Updated Balance =", balance)

elif choice == 3:

    withdraw = float(input("Enter Withdrawl Amount :"))

    balance = balance - withdraw

    print("Updated Balance =", balance)

else:
    print("Invalid Choice")

# =======================================================================================
# Dictionary-
# =======================================================================================

account_holder = {
    "Holder Name": name,
    "Age": age,
    "Sex": sex,
    "Address": add,
    "Bank Name": bank_name,
    "Branch Name": branch_name,
    "A/c Number": account_number,
    "Total Balance": balance,
}

# =======================================================================================

print("\n===== Account Holder Details =====")
print("Account Holder :", account_holder["Holder Name"])
print("Age :", account_holder["Age"])
print("Sex :", account_holder["Sex"])
print("Address :", account_holder["Address"])
print("Bank Name :", account_holder["Bank Name"])
print("Branch Name :", account_holder["Branch Name"])
print("Account Number :", account_holder["A/c Number"])
print("Total Balance :", account_holder["Total Balance"])

# =======================================================================================
