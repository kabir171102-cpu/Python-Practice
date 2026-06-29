# =======================================================================================
print("==== Electricity Bill System ====")
# =======================================================================================

name = input("Enter Name :")
age = int(input("Enter Age :"))
add = input("Enter Address :")
connection_from = input("Enter Connection Detail :")


print(f"""
Customer Name : {name}
Age : {age}
Address : {add}
Connection From : {connection_from}
      """)

# =======================================================================================
# Units Consumed-
# =======================================================================================

units = float(input("Enter Units :"))
rate_per_units = float(input("Enter Rate Per Units :"))
fixed_charge = float(input("Enter Fixed Charge :"))
tax = float(input("Enter Tax Percentage :"))


print("Units Consumed =", units)
print("Rate Per Units =", rate_per_units)
print("Fixed Charge =", fixed_charge)
print("Tax =", tax, "Percentage")
print("\n")

# =======================================================================================
# Unit Charge-
# =======================================================================================

unit_charge = units * rate_per_units

# =======================================================================================
# subtotal-
# =======================================================================================

subtotal = unit_charge + fixed_charge

# =======================================================================================
# Tax-
# =======================================================================================

tax_charge = (subtotal * tax) / 100

# =======================================================================================
# Final Bill-
# =======================================================================================

final_bill = subtotal + tax_charge

# =======================================================================================

print("\n")
print("Unit Charge =", unit_charge)
print("Subtotal =", subtotal)
print("Tax Charge=", tax_charge)
print("Final Bill =", final_bill)

# =======================================================================================

print("\n")
bill_status = input("Enter Status :")

if bill_status.lower() == "paid":
    status = "Final Bill = Paid"
else:
    status = "Final Bill = Unpaid"

print(status)

print("\n")

# =======================================================================================
# Dictionary-
# =======================================================================================

electricity = {
    "Customer Name": name,
    "Age": age,
    "Address": add,
    "Connection From": connection_from,
    "Total Units": units,
    "Rate Per Units": rate_per_units,
    "Fixed Charge": fixed_charge,
    "Tax Percentage": tax,
    "Units Charge": unit_charge,
    "SubTotal": subtotal,
    "Tax Charge": tax_charge,
    "Final Bill": final_bill,
    "Status": status,
}
print(electricity)

# =======================================================================================

print("\n ==== Electricity Bill System ==== ")
print("Customer Name :", electricity["Customer Name"])
print("Age :", electricity["Age"])
print("Address :", electricity["Address"])
print("Connection From :", electricity["Connection From"])
print("Total Units :", electricity["Total Units"])
print("Rate Per Units :", electricity["Rate Per Units"])
print("Fixed Charge :", electricity["Fixed Charge"])
print("Tax Percentage :", electricity["Tax Percentage"])
print("Units Charge :", electricity["Units Charge"])
print("SubTotal :", electricity["SubTotal"])
print("Tax Charge :", electricity["Tax Charge"])
print("Final Bill :", electricity["Final Bill"])
print("Status :", electricity["Status"])

# =======================================================================================
