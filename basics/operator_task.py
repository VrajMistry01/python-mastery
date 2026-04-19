def calculate(a: int, b: int, operator: str):
    operator_list = ["+", "-", "*", "/", "//", "%", "**"]

    if operator not in operator_list:
        return "Please enter a valid operator"

    # single zero check (cleaner)
    if operator in ["/", "//", "%"] and b == 0:
        return "Cannot divide by zero!"

    if operator == "+":
        return a + b

    elif operator == "-":
        return a - b

    elif operator == "*":
        return a * b

    elif operator == "/":
        return a / b

    elif operator == "//":
        return a // b

    elif operator == "%":
        return a % b

    elif operator == "**":
        return a ** b


# -------------------------------
# TEST CASES (mandatory)
# -------------------------------

print(calculate(10, 3, "+"))
print(calculate(10, 3, "/"))
print(calculate(10, 0, "/"))
print(calculate(10, 0, "%"))
print(calculate(10, 3, "abc"))
print(calculate(2, 10, "**"))