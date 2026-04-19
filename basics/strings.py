# Raw input (note the extra spaces)
user_input = " hello world "
print(len(user_input))   # 13 (includes spaces)

# Convert to uppercase
clean_text = user_input.upper()
print(clean_text)        # " HELLO WORLD "

# Convert to lowercase
clean_text = clean_text.lower()
print(clean_text)        # " hello world "

# Remove extra spaces from start and end
clean_text = clean_text.strip()
print(clean_text)        # "hello world"

# Split into words
words = clean_text.split(" ")
print(words)             # ['hello', 'world']

# Replace text
updated_text = clean_text.replace("hello", "hi")
print(updated_text)      # "hi world"

# Find position of a word
position = clean_text.find("world")
print(position)          # 6

# Check if word exists
contains_hello = "hello" in clean_text
print(contains_hello)    # True


# -------------------------------------
# String formatting examples

person_name = "Vraj"
person_age = 20

# Recommended (f-string)
print(f"My name is {person_name} and I am {person_age}")

# Using .format()
print("My name is {} and I am {}".format(person_name, person_age))

# Old style (not recommended)
print("My name is %s and I am %d" % (person_name, person_age))


# -------------------------------------
# String slicing examples

language = "python"

print(language[1:4])   # "yth"
print(language[-3:])   # "hon"
print(language[::-1])  # "nohtyp" (reverse)
print(language[::2])   # "pto"
print(language[::-3])  # "nt"


# Index reference:
#  p  y  t  h  o  n
#  0  1  2  3  4  5
# -6 -5 -4 -3 -2 -1


# string immutability example
original_string = "immutable"

# This creates a new string (original is unchanged)
new_string = original_string.replace("a", "o")

print(original_string)  # "immutable"
print(new_string)       # "immutoble"