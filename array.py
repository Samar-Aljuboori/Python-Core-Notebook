# Lists vs Arrays in Python
# ----------------------------------------------------------------------------
# In Python, we usually use 'Lists' because they are extremely flexible.
# 'Arrays' are only used when we need strict type control and high performance.
# ----------------------------------------------------------------------------


import array # Importing Python's built-in array module

# ------------------------------------------------------------------------------
# SECTION 1: The Python List (The Magical Flexible Box)
# - Can hold different types of data at the same time (Strings, Numbers, etc.)
# - Can grow or shrink in size automatically.
# ------------------------------------------------------------------------------

print("--- SECTION 1: PYTHON LISTS ---")

# Example 1: Creating a list with mixed data types
my_flexible_list = ["Python", 3, 98.5, True]
print(f"Example 1 List: {my_flexible_list}") 
# -> Output: Example 1 List: ['Python', 3, 98.5, True]


# Example 2: Lists are dynamic (we can easily add items)
my_flexible_list.append("New Item")
print(f"Example 2 (After append): {my_flexible_list}")
# -> Output: Example 2 (After append): ['Python', 3, 98.5, True, 'New Item']


# ------------------------------------------------------------------------------
# SECTION 2: The Python Array (The Strict Fixed Box)
# - Must be imported using 'import array'.
# - Can ONLY hold ONE specific type of data (e.g., ONLY integers, ONLY floats).
# - Saves memory and is faster for large mathematical calculations.
# ------------------------------------------------------------------------------

print("\n--- SECTION 2: PYTHON ARRAYS ---")

# Example 3: Creating an Integer Array
# Note: 'i' means this array can ONLY hold signed integers ( أرقام صحيحة موجبة).
my_strict_array = array.array('i', [10, 20, 30, 40])
print(f"Example 3 Array: {my_strict_array}")
# -> Output: Example 3 Array: array('i', [10, 20, 30, 40])


# Example 4: Adding the correct data type works perfectly
my_strict_array.append(50)
print(f"Example 4 (After valid append): {my_strict_array}")
# -> Output: Example 4 (After valid append): array('i', [10, 20, 30, 40, 50])


# Example 5: CRITICAL RULE - Trying to add a String to an Integer Array triggers a TypeError!
print("Example 5: Demonstrating strict type restriction in arrays:")

# The line below is commented out because it is FORBIDDEN and will crash the program.
# my_strict_array.append("Hello") 

print("Result: Cannot append a string to an integer array. Python strictly blocks it!")
# -> Output: Result: Cannot append a string to an integer array. Python strictly blocks it!
# -> If un-commented, it raises: TypeError: an integer is required (got type str)


# ------------------------------------------------------------------------------
# SECTION 3: Essential Array Operations (Methods)
# ------------------------------------------------------------------------------

# Creating a baseline float array ('d' means double/float - أرقام عشرية)
prices = array.array('d', [10.5, 20.9, 30.0, 40.5])

# Example 6: Accessing and Modifying items by Index
print("Example 6:")
print(f"First item: {prices[0]}")  # -> Output: First item: 10.5
prices[1] = 25.5                   # Changing 20.9 to 25.5
print(f"Updated array: {prices}") # -> Output: Updated array: array('d', [10.5, 25.5, 30.0, 40.5])

print("-" * 40)

# Example 7: Removing items (remove) and popping by index (pop)
print("Example 7:")
prices.remove(30.0)                # Removes the value 30.0
print(f"After remove: {prices}")   # -> Output: After remove: array('d', [10.5, 25.5, 40.5])

popped_item = prices.pop(0)        # Removes and returns the item at index 0
print(f"Popped item: {popped_item}") # -> Output: Popped item: 10.5
print(f"After pop: {prices}")      # -> Output: After pop: array('d', [25.5, 40.5])

print("-" * 40)

# Example 8: Slicing an Array (Getting a sub-array)
print("Example 8:")
numbers = array.array('i', [10, 20, 30, 40, 50])
print(numbers[1:4])                # -> Output: array('i', [20, 30, 40])

print("-" * 40)

# Example 9: Searching for an item's position (index)
print("Example 9:")
# Finds the index of the value 40
print(f"Index of 40: {numbers.index(40)}") # -> Output: Index of 40: 3


# ------------------------------------------------------------------------------
# SECTION 4: Understanding Typecodes (The Python Array Dictionary)
# When creating an array, the first letter defines what type of data goes inside:
#
# 'b' -> Represents signed char (Integer of 1 byte)
# 'i' -> Represents signed integer (Integer of 2 or 4 bytes) - Most Common for Whole Numbers
# 'f' -> Represents floating-point (Decimal numbers of 4 bytes)
# 'd' -> Represents double precision floating-point (Decimal numbers of 8 bytes) - Most Common for Decimals
# ------------------------------------------------------------------------------

print("\n--- Array Typecode Cheat Sheet ---")
print(f"The integer array typecode is: '{numbers.typecode}'")
 # -> Output: The integer array typecode is: 'i'
print(f"The float array typecode is: '{prices.typecode}'")
 # -> Output: The float array typecode is: 'd'