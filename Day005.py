# Day 005: List Operations in Python
# --------------------------------
# These notes explain common list manipulation methods: del, remove, pop, and clear.

# Example list
a = [1, 2, 3, 4, 5, 6, 7]
# del a[5]
# 'del' removes an item at a specific index.
# Example: del a[5] would delete the value 6 from the list.

# remove(): removes the FIRST matching value from the list
a = [1, 2, 3, 4, 5, "sudan", "sudan"]
a.remove("sudan")  # Removes the first occurrence of 'sudan'
a.remove("sudan")  # Removes the second occurrence
# If the value is not found, remove() raises an error.

# pop(): removes AND returns an item from the list
b = a.pop()         # Removes the last item in the list
print(a)            # List after popping the last element
print(b)            # Shows the popped element

# pop(index): removes and returns an item at a specific index
data = ['suman', 'hari', 'ramesh']
pop_data = data.pop(1)  # Removes 'hari' because it's at index 1
print(data)             # ['suman', 'ramesh']
print(pop_data)         # 'hari'
print()

# clear(): removes all elements from the list
data3 = ['1', 2, 3, 4, 5]
data3.clear()           # Empties the entire list
print(data3)            # Output: []