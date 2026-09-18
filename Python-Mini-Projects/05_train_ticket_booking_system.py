# =======================================================================================
print("==== Train Ticket Booking System ====")
# =======================================================================================

Passenger_name = input("Enter Name :")
age = int(input("Enter Age :"))
sex = input("Enter Sex :")
source = input("Enter Source :")
destination = input("Enter Destination :")

print(f"""
Passenger Name : {Passenger_name}
Age : {age}
Sex : {sex}
Source : {source}
Destination : {destination}

      """)

# =======================================================================================
print("1. General Ticket = 150")
print("2. Sleeper Ticket = 450")
print("3. AC Ticket = 1200")
# =======================================================================================

choice = int(input("Enter Choice :"))

# =======================================================================================
# Ticket-
# =======================================================================================

if choice == 1:
    print("General Ticket = 150rs")
elif choice == 2:
    print("Sleeper Ticket = 450rs")
elif choice == 3:
    print("AC Ticket = 1200rs")
else:
    print("Unavailable")

# =======================================================================================
# Seat Type-
# =======================================================================================

if choice == 1:
    seat_type = "General"
elif choice == 2:
    seat_type = "Sleeper"
elif choice == 3:
    seat_type = "AC"
else:
    seat_type = "Invalid Choice"

print("Seat Type =", seat_type)

# =======================================================================================
# Dictionary-
# =======================================================================================

ticket = {
    "Passenger Name": Passenger_name,
    "Age": age,
    "Sex": sex,
    "Source": source,
    "Destination": destination,
    "Seat Type": seat_type,
}

print(ticket)

# =======================================================================================

print("\n==== Train Ticket Booking System ====")
print("\n")
print("Passenger Name :", ticket["Passenger Name"])
print("Age :", ticket["Age"])
print("Sex :", ticket["Sex"])
print("Souce :", ticket["Source"])
print("Destination :", ticket["Destination"])
print("Choice =", choice)
if choice == 1:
    print("General Ticket Confirmed : 150rs")
elif choice == 2:
    print("Sleeper Ticket Confirmed = 450rs")
elif choice == 3:
    print("AC Ticket Confirmed = 1200rs")

print("Seat Type =", ticket["Seat Type"])

# =======================================================================================
