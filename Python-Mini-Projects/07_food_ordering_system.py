# =======================================================================================
print("==== Food Ordering System ====")
# =======================================================================================

name = input("Enter Name :")
mob_no = int(input("Enter Mobile No :"))
gender = input("Enter Gender :")
add = input("Enter Address :")

print(f"""
Customer Name : {name}
Mobile No : {mob_no}
Gender : {gender}
Address : {add}
      """)

# =======================================================================================
# Menu Card-
# =======================================================================================

print("\n")
print("A. Paneer Rice")
print("B. Paneer Chilli")
print("C. Veg Momos")
print("D. Veg-Biryani")
print("E. Hakka Noodles")

# =======================================================================================
# Food Selection-
# =======================================================================================

choice = input("Enter Food Choice :")
print("Choice Food =", choice)

# =======================================================================================

if choice.lower() == "a":
    food = "Paneer Rice"
    price = 120
    qty = int(input("Enter Food Quantity :"))
elif choice.lower() == "b":
    food = "Paneer Chilli"
    price = 150
    qty = int(input("Enter Food Quantity :"))
elif choice.lower() == "c":
    food = "Veg Momos"
    price = 70
    qty = int(input("Enter Food Quantity :"))
elif choice.lower() == "d":
    food = "Veg- Biryani"
    price = 110
    qty = int(input("Enter Food Quantity :"))
elif choice.lower() == "e":
    food = "Hakka Noodles"
    price = 60
    qty = int(input("Enter Food Quantity :"))
else:
    food = "Unavailable"
    price = 0
    qty = 0

print("Food =", food)
print("Price =", price)
print("Quantity =", qty)

# =======================================================================================
# Bill-
# =======================================================================================

food_total = price * qty
gst_percentage = int(input("Enter GST Percentage :"))
gst_amount = (food_total * gst_percentage) / 100
final_bill = food_total + gst_amount

print("Food Total =", food_total)
print("GST % =", gst_percentage)
print("GST Amount =", gst_amount)
print("Final Bill =", final_bill)

# =======================================================================================
# Payment-
# =======================================================================================

payment_status = input("Enter Payment Status :")
print(payment_status)

# =======================================================================================

if payment_status.lower() == "paid":
    print("Final Payment = Paid")
else:
    print("Final Payment = Unpaid")

print("\n")

# =======================================================================================
# Dictionary-
# =======================================================================================

order = {
    "Customer Name": name,
    "Mobile No": mob_no,
    "Gender": gender,
    "Address": add,
    "Choice": choice,
    "Food": food,
    "Quantity": qty,
    "Price": price,
    "Food Total": food_total,
    "GST %": gst_percentage,
    "GST Amount": gst_amount,
    "Final Bill": final_bill,
    "Payment Status": payment_status,
}

print(order)

# =======================================================================================

print("\n==== Food Ordering System ====")
print("Customer Name :", order["Customer Name"])
print("Mobile No :", order["Mobile No"])
print("Gender :", order["Gender"])
print("Address :", order["Address"])
print("Choice :", order["Choice"])
print("Food :", order["Food"])
print("Quantity :", order["Quantity"])
print("Price :", order["Price"])
print("Food Total :", order["Food Total"])
print("GST % :", order["GST %"])
print("GST Amount :", order["GST Amount"])
print("Final Bill :", order["Final Bill"])
print("Payment Status :", order["Payment Status"])

# =======================================================================================
