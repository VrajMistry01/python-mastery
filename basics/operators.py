
# -------------------------------
# 1. ARITHMETIC OPERATORS
# -------------------------------

a = 10
b = 3

print("Arithmetic Operators:")
print("Addition (+):", a + b)        # 13
print("Subtraction (-):", a - b)     # 7
print("Multiplication (*):", a * b)  # 30
print("Division (/):", a / b)        # 3.333...
print("Floor Division (//):", a // b) # 3
print("Modulus (%):", a % b)         # 1
print("Exponent (**):", a ** b)      # 1000


# -------------------------------
# 2. HOURS ↔ MINUTES CONVERSION
# -------------------------------

hours = 5
minutes = hours * 60

print("\nTime Conversion:")
print(f"{hours} hours = {minutes} minutes")

total_minutes = 350
converted_hours = total_minutes // 60
remaining_minutes = total_minutes % 60

print(f"{total_minutes} minutes = {converted_hours} hours and {remaining_minutes} minutes")


# -------------------------------
# 3. SHORT-CIRCUIT EVALUATION
# -------------------------------

print("\nShort-Circuit Evaluation:")

# AND → returns first falsy OR last truthy
print(0 and 5)         # 0
print(5 and 10)        # 10

# OR → returns first truthy OR last falsy
print(0 or 5)          # 5
print("" or "Hello")   # Hello
print("Hi" or "World") # Hi


# -------------------------------
# 4. // vs int() WITH NEGATIVES
# -------------------------------
#5//2 this doesnt give Quatient but floor value of actual devision
print("\nFloor Division vs int() with negatives:")

x = -7
y = 3

print("x // y:", x // y)        # -3 (floors down)
print("int(x / y):", int(x / y)) # -2 (truncates toward 0)
d = -7
e = -3

print("d // e:", d // e)        #2 both gives same
print("int(d / e):", int(d / e)) # 2


# -------------------------------
# SUMMARY (MENTAL MODEL)
# -------------------------------

"""
Key Differences:

1. // → floor (goes to smaller integer)
2. int() → truncates (cuts decimal toward zero)

Example:
-7 / 3 = -2.33

//  → -3
int → -2
"""