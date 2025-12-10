# Day 007: Membership Operators, Loops, and Iteration in Python
# ------------------------------------------------------------

# Membership Operators
# 'in' checks if an element exists in a list or dictionary values
# 'not in' checks if an element does NOT exist in a list or dictionary values

# Example with list
a = [1, 2, 3, 4, 5, 6]
print(7 not in a)  # True, because 7 is not in the list

# Example with dictionary
data = {
    "name": "madan",
    "surname": "bhandari"
}
print("bhandari" in data.values())  # True, checks among the dictionary's values

# Access dictionary values safely
# data['name'] or data.get('name')


# For Loop Basics
# Loop over items in a list or string
for i in [1, 2, 3, 4, 5]:
    print(i + i)  # Prints double of each number

for char in "broadway":
    print(char)   # Prints each character

# Using range(start, stop, step)
for i in range(-10, -1, 1):
    print(i)      # Iterates from -10 to -2


# Collecting even and odd numbers from a range
even = []
odd = []
for i in range(100, 120):
    if i % 2 != 0:
        odd.append(i)
    else:
        even.append(i)

print("Odd numbers:", odd)
print("Even numbers:", even)

# Merge lists and sort in reverse
even.extend(odd)
even.sort(reverse=True)
print(even)


# Using 'continue' in loops
for i in [1,2,3,4,5,6,7,8]:
    if i == 4:
        continue  # Skips the rest of the loop when i == 4
    print(i)

# Filtering non-integers and booleans from a list
data = [1, "sudan", 2, 3, 4, 5, True, "bhandari", 5, 6]
for i in data:
    if not isinstance(i, int) or isinstance(i, bool):
        continue
    print(i)


# Sum of list elements
numbers = [1, 2, 3, 4, 5, 6, 7]
sum_val = 0
for i in numbers:
    sum_val += i
print("Sum is", sum_val)


# Nested loops example
for i in [1, 2, 3]:
    for j in [4, 5, 6]:
        print(i, j)  # Prints all combinations of i and j