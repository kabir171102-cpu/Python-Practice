# ======================================================================================
# Temperature Converter-
# ======================================================================================

print("1. Celsius to Fahrenheit")
print("2. Celsius to Kelvin")
print("3. Fahrenheit to Celsius")
print("4. Kelvin to Celsius")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    c = float(input("Enter Celsius: "))
    f = (9 / 5) * c + 32
    print("Fahrenheit =", f)

elif choice == 2:
    c = float(input("Enter Celsius: "))
    k = c + 273.15
    print("Kelvin =", k)

elif choice == 3:
    f = float(input("Enter Fahrenheit: "))
    c = (5 / 9) * (f - 32)
    print("Celsius =", c)

elif choice == 4:
    k = float(input("Enter Kelvin: "))
    c = k - 273.15
    print("Celsius =", c)

else:
    print("Invalid choice")

# =======================================================================================
# Fahrenheit to Kelvin
# =======================================================================================

f = float(input("Fahrenheit: "))
k = (5 / 9) * (f - 32) + 273.15
print("Kelvin =", k)

# =======================================================================================
# Kelvin to Fahrenheit
# =======================================================================================

k = float(input("Kelvin: "))
f = (9 / 5) * (k - 273.15) + 32
print("Fahrenheit =", f)
