"""
Beginner-Friendly Python Notes
This file rewrites your original notes in a clean, organized, and easy-to-understand way.
Comments explain each concept step-by-step.
"""

# ----------------------------------------
# 1. PRINTING BASIC OUTPUT
# ----------------------------------------

# The print() function displays text or values on the screen.
print("hello world")
print("hello world")  # You can print as many times as you want
 
#  You can also print multiple items together.
# Here, we are printing a string and the result of a math expression.
print("sum ", 1 + 2, "math")


# ----------------------------------------
# 2. VARIABLES AND SIMPLE MATH
# ----------------------------------------

# A variable stores a value. You can reuse it anytime.
a = 2
b = 3

# Adding two variables
print(a + b)  # Output: 5


# ----------------------------------------
# 3. VALID VARIABLE NAMES
# ----------------------------------------
# Python variable naming rules:
# - Can contain letters, numbers, and underscores
# - Cannot start with a number
# - Cannot use special characters like $, @, %, etc.
# - Cannot use reserved keywords (like 'while', 'print', etc.)

abcd = 1
TEST = 1          # Uppercase is allowed
teSt = 1          # Mixed case allowed
_test = 1         # Starts with underscore → valid
test_test = 1     # Underscores allowed
test_test_test = 1
test2 = 1         # Numbers allowed but NOT at the beginning

# Updating the value of a variable
teSt = 3
print(teSt)  # Shows updated value


# ----------------------------------------
# 4. INVALID VARIABLE NAMES (DO NOT USE)
# ----------------------------------------
# The following examples are invalid and will cause errors:

# while = 1      # Invalid: 'while' is a reserved keyword in Python
# print = 1      # Invalid: overrides built-in print function
# $yes = 1       # Invalid: variable names can't contain '$'
# 2test = 1      # Invalid: cannot start with a number

# ----------------------------------------
# End of notes
# ----------------------------------------
