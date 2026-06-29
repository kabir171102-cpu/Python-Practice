# """Let's Practice"""
# ==========================================================================================
# Question 1- Store following word meanings in a python dictionary:
#       table: "a piece of furniture", "list of facts & figures"
#       cat: "a small animal"
# ==========================================================================================

store = {
    "table": ("a piece of furniture", "list of facts & figures"),
    "cat": ("a small animal"),
}

# ==========================
# Print Variable & keys
# ==========================

print(store)
print(type(store))
print(store.keys())
print(list(store.keys()))

# ==========================
# Print Values & Items
# ==========================

print(store.values())
print(list(store.values()))
print(tuple(store.values()))
print(str(store.values()))
print(store.items())
print(list(store.items()))
print(tuple(store.items()))
print(str(store.items()))

# ==========================
# Get  Values of Keys
# ==========================

print(store.get("cat"))
print(store.get("table"))

# ==========================
# Update Keys - Values
# ==========================

store.update({"cat": "billi"})
print(store)

# ==========================
# Update New Variable
# ==========================
new_store = {"cat": "bagadBilli"}
store.update(new_store)
print(store)
print(type(new_store))

# ==========================================================================================
