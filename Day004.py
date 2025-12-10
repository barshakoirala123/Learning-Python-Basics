
# Day004 :If-else, nested conditions, grading system, 
# validation, ternary operator, isinstance

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
print(5%2)    # Modulus (remainder when divided by 2)

# Concatenating numeric-looking strings
print("1" + "1")  # Output: "11"

# Comparison operators examples
print(5 == "5")  # Checks equality; int vs string returns False
# ==  equality
# !=  not equal
# >=  greater than or equal
# <=  less than or equal
# >   greater than
# <   less than

a = 1
A = 1  # Variable names are case-sensitive; 'a' and 'A' are different variables

# Logical operators
# and  returns True only if both conditions are True
# or   returns True if at least one condition is True
# not  reverses a boolean value

print(True and True)   # Both True -> True
print(True or False)   # One True -> True
print(False or True)   # One True -> True
print(not(False))      # not False -> True

# Shorthand operators (augmented assignment)
# a += 3   means a = a + 3
# a -= 1   means a = a - 1

# Example values
a = 1
b = 1

print(a + b)        # Addition
print(a == b)       # Equality check
print(a == b and b > a)  # Logical AND combining comparisons

a += b              # Adds b to a
print(a)            # Updated value of a

# --------------------------------------------
# Conditional statements with improved explanations
# --------------------------------------------
'''
General structure of conditional statements:
if(condition):
    code block
elif(condition):
    code block
elif(condition):
    code block
else:
    code block
'''

# Example structure
# a = 2
# if a == 1:
#     print("first")
# elif a == 2:
#     print("second")

# Checking even or odd
# a = int(input("Enter a number "))
# if a % 2 == 0:
#     print(f"{a} is even")
# else:
#     print(f"{a} is odd")

# Percentage grading system with multiple conditions
# a = float(input("Enter Your Percentage: "))
# if 80 <= a <= 100:
#     print(f'You have passed in first division with distinction with {a}%')
# elif 60 <= a < 80:
#     print(f'You have passed in first division with {a}%')
# elif 45 <= a < 60:
#     print(f'You have passed in second division with {a}%')
# elif 35 <= a < 45:
#     print(f'You have passed in third division with {a}%')
# elif 0 <= a < 35:
#     print(f'You have failed your exam with {a}%')
# else:
#     print(f'Invalid input, please try again')

# Nested IF example
'''
nested-if pattern:
if(condition):
    if(condition):
        code block
    else:
        code block
else:
    if(condition):
        code block
'''

if 1 == 1:
    if 1 == 1:
        print("1 is here")
    else:
        print("else is here")
    print("i am if")
else:
    print("1st else is here")

# Nested-if program for discounts (assignment example provided)
'''
Create a nested-if program for shop discount.
If purchase is above 1000:
    If customer has membership -> 20% discount
    Else -> 10% discount
Print the applicable discount.
'''

# Gender identification
gender = "F"
if gender == "M":
    print("Male")
else:
    print("Female")

# Using ternary operator for concise conditional assignment
a = "Male" if gender == "M" else "Female"
print(a)

# Type checking example
a = 1
print("type check", isinstance(a, str))
if isinstance(a, int):
    print("number is int")

print("--------------------")

# Validating percentage input before converting
a = "1"
if not a.isalpha():  # Ensures the input doesn't contain letters
    a = float(a)
    if 80 <= a <= 100:
        print(f'You have passed in first division with distinction with {a}%')
    elif 60 <= a < 80:
        print(f'You have passed in first division with {a}%')
    elif 45 <= a < 60:
        print(f'You have passed in second division with {a}%')
    elif 35 <= a < 45:
        print(f'You have passed in third division with {a}%')
    elif 0 <= a < 35:
        print(f'You have failed with {a}%')
    else:
        print("Your input is out of valid range")
else:
    print("Provide a valid number")

# String case formatting
data = "suDan"
print(data.title())
