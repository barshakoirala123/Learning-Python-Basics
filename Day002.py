# Day 002: Python: Comparison, Logical Operators and 
# Shorthand Assignments

# Data types

# Integer assignment
a = 1
abcd = 1

# Number types available in Python
# int: Whole numbers
# float: Decimal numbers

# Assigning an integer
a = 1

# Assigning a float
a = 1.0

# String examples
# Strings can be enclosed in double quotes, single quotes, or triple quotes
a = "1"
a = '1'
a = ''' 1.0  '''

# Another string example
a = "broadway education"

# Multiline string assignment using triple quotes
a = '''
asda
das
das
'''

# Even if a string looks like a number, it's still a string
a = "50.0"
print(type(a))  # Output: <class 'str'>

# Examples of different data types
a = 122          # int
b = 112.31       # float
c = "test"       # str

print(type(a), type(b), type(c))

# Complex number assignment
a = 2+3j
print(type(a))   # Output: <class 'complex'>

# Special data types
a = "None"       # string containing the word 'None'
b = None         # actual NoneType
c = True         # boolean
d = False        # boolean

print(type(b), type(c))  # <class 'NoneType'> <class 'bool'>

# Boolean variables
is_active = True
has_document = True
kyc_verified = True

# Variable naming demonstration
test_test_test = 1

# Taking input from user (commented out)
# a = input("Enter a number .. ")
# c = int(a)

# Basic string concatenation
name = "sudan"
greeting = "hello "
message = "your due amount is "
amount = 60

# Printing concatenated strings and variables
print(greeting, name, message, amount)

# Using f-string for formatted output
print(f'{greeting}                             {2+2}')

# Basic arithmetic operations
a = 10
b = 16
print(a+b, a-b)  # Addition and subtraction

# Division example
a = 4
b = 1
print(a/b)  # Division always returns float

# String concatenation
a = "hello "
b = "hi"
print(a + " " + b)  # Joining strings

# Replicating a string
print(a * 2)  # Prints "hello hello "
print("here")

# Floor division, exponent, modulus
print(5//2)   # Floor division (result: 2)
print(5**3)   # Exponentiation (5^3 = 125)
print(5 % 2)    # Modulus (remainder when divided by 2)

# Concatenating numeric-looking strings
print("1" + "1")  # Output: "11"
# Note: To perform arithmetic on numeric strings, convert them to int or float first
# Example of converting string to int
num_str = "50"
num_int = int(num_str)
print(num_int + 10)  # Output: 60
# Example of converting string to float
num_str_float = "50.5"
num_float = float(num_str_float)
print(num_float + 10)  # Output: 60.5

# ----------------------------------------
# End of notes
# ----------------------------------------
