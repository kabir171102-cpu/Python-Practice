# =======================================================================================
# Question - Exercise on exception handling

# Define a function named calculator.
# - It will ask for a mathematical operation from the user.
# - An operation is something like this: (6 * 5)

# Thefunction will get this input and do the necessary calculation, 
# and return the result as follows:
# 6 * 5 = 30
# - The operation type can only be one of these: (+, -, *, /)

# Exception handling for possible errors:-
# 1- Two operands and operator hould be there.Else, raise exception.
# 2- Operator must be part of (+, -, *, /)
# 3- operator must be castable into float.
# 4- zerodivision error while division.
# =======================================================================================

class OperationError(Exception):
    pass

class OperatorError(Exception):
    pass

def calculator():
    operations = ("+", "-", "*", "/")
    try:
        user_input = input("Please enter an operation: ")
        elements = user_input.split()
        if len(elements) != 3:
            raise OperationError("Please enter two operands and an operator in between "
            "separated by spaces.")
        operator = elements[1]
        if operator not in operations:
            raise OperationError(f"{operator} is not valid, please enter an operator from {operations}")
        num1 = float(elements[0])
        num2 = float(elements[2])
        if operator == "/" and num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
    except Exception as e:
        print(e)
        print("Try Again!")
        calculator()
    else:
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            result = num1 / num2

    finally:
        return f"{num1} {operator} {num2} =  {result}"

result = calculator()
print(result)