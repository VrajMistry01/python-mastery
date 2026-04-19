def calculate(a: int, b: int, operator: str) -> int:
    operator_list = ["+", "-", "*", "/", "//", "%", "**"]

    if operator not in operator_list:
        return "Please enter a valid operator"

    if operator == "+":
        return a + b

    elif operator == "-":
        return a - b

    elif operator == "*":
        return a * b

    elif operator == "/":
        if b == 0:
            return "Cannot divide by zero!"
        return a / b

    elif operator == "//":
        if b == 0:
            return "Cannot divide by zero!"
        return a // b

    elif operator == "%":
        if b == 0:
            return "Cannot divide by zero!"
        return a % b

    elif operator == "**":
        return a ** b