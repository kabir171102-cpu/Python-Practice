# =======================================================================================
print("==== Recharge System ====")
# =======================================================================================

name = input("Enter customer name :")
mob_no = int(input("Enter mobile no :"))
curr_balance = int(input("Enter current balance :"))

print(f"""
Customer Name : {name}
Mobile No : {mob_no}
Current Balance : {curr_balance,'rs'}
      """)

# =======================================================================================
print("1. Plan of 199rs for 21 Days")
print("2. Plan of 299rs for 28 Days")
print("3. Plan of 899rs for 84 Days")
# =======================================================================================
print("\n")
choice = int(input("Enter the choice no :"))
# =======================================================================================

if choice == 1:
    if curr_balance >= 199:
        curr_balance = curr_balance - 199
        print("Recharge Succesful of 199rs")
        print("Available Balance =", curr_balance)
    else:
        print("Insufficient Balance")

# =======================================================================================

if choice == 2:

    if curr_balance >= 299:
        curr_balance = curr_balance - 299
        print("Recharge Successful of 299rs")
        print("Available Balance =", curr_balance)

    else:
        print("Insufficient Balance")

# =======================================================================================

if choice == 3:

    if curr_balance >= 899:
        curr_balance = curr_balance - 899
        print("Recharge Successful of 899rs")
        print("Available Balance =", curr_balance, "rs")

    else:
        print("Insufficient Balance")

# =======================================================================================
# Dictionary-
# =======================================================================================

recharge = {
    "Customer Name": name,
    "Mobile No": mob_no,
    "Available Balance": curr_balance,
    "Plan Choice": choice,
}

print(recharge)

# =======================================================================================

print("\n")

print("\n ==== Recharge System ==== ")
print("Customer Name :", recharge["Customer Name"])
print("Mobile Number :", recharge["Mobile No"])
print("Available Balance :", recharge["Available Balance"])
print("Plan Choice :", recharge["Plan Choice"])
print("\n1. Plan of 199rs for 21 Days")
print("2. Plan of 299rs for 28 Days")
print("3. Plan of 899rs for 84 Days")
if choice == 1:
    print("Recharge Successful of 199rs")
elif choice == 2:
    print("Recharge Successful of 299rs")
elif choice == 3:
    print("Recharge Successful of 899rs")
else:
    ("Invalid Choice")
print(curr_balance, "rs")

# =======================================================================================
