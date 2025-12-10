# Day 006: Nested Lists, Dictionaries, and Data Access
# ---------------------------------------------------
# This note explains how to work with nested lists, nested dictionaries,
# and basic dictionary operations including keys, values, update, pop, and get.

# Nested list example
# A list can contain other lists or dictionaries as elements.
# Accessing nested elements uses multiple indices.
# Example: data[2][4][0] means:
#   - take the 3rd element of 'data' (index 2)
#   - then take its 5th element (index 4)
#   - then take its first element (index 0)

data = [
    {"name": "sudan"},
    10,
    [
        1,
        2,
        [3],
        4,
        [5],
        6,
        7,
    ],
]

print(data[2][4][0])  # Output: 5

# Another nested list example
# Shows a complex list with sublists inside sublists
# Flattening is conceptual here; we are not using a flatten function
a = [1, 2, 3, [1, 1, 2, 1, 1, [1]]]
# Expected conceptual output if flattened: 1,2,3,1,1,2,1,1,1


# Dictionary basics
# A dictionary stores key-value pairs. Keys are unique.
boy = {
    "name": [1, 2],      # Values can be lists
    "age": 21,           # Integer value
    "height": 6,         # Integer value
    "weight": 68,        # Integer value
    "city": "Peshawar",  # String value
    "religion": "Muslim"  # String value
}

print(type(boy))       # <class 'dict'>
print(len(boy))        # Number of key-value pairs in the dictionary
print(boy["religion"])  # Access value using key
print(boy)             # Print entire dictionary


# Nested dictionary example
# A dictionary can contain another dictionary as a value
boy1 = {
    "name": [1, 2],
    "age": 21,
    "height": 6,
    "weight": 68,
    "city": {
        "temp": "kathmandu",  # Nested dictionary
        "per": "dang",
    },
    "religion": "Muslim",
}


# More complex dictionary example with list of dictionaries
# Useful for storing structured data like phone numbers
data = {
    "name": "Suman",
    "address": "Nepal",
    "phone_number": [
        {"type": "Jio", "number": "9844"},
        {"type": "Idea", "number": "98062"},
        {"type": "NTC"},  # Key 'number' may be missing
    ],
}

# Access dictionary keys and values
print(data.keys())     # Shows all the keys
print("----------------------------------------------------")
print(data.values())   # Shows all the values

print(".." * 120)     # Just a visual separator

# Modifying dictionary entries
std = {
    "name": "suman",
    "address": "nepal",
}

std["name"] = 123           # Update a key's value
std.update({"name": "hari", "number": "123"})  # Update multiple keys

# Removing items from dictionary
std.pop("number")           # Removes a specific key-value pair
std.popitem()                # Removes last inserted key-value pair
print(std)

# Accessing values safely
print(std["name"])          # Access value directly (will error if key missing)
print(std.get("name"))      # Safe access, returns None if key is missing


# Task: Take 5 integer inputs from the user, store in a list, sum them, and calculate percentage
# This involves using string methods, checking isdigit(), logical operations, list manipulation,
# comparison operators, input handling, data type conversion, and if conditions
