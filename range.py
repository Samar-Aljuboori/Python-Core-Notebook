#  Complete Guide to the range() Function in Python

# ------------------------------------------------------------------------------
# SECTION 1: Understanding range() Syntax
# Syntax: range(start, stop, step)
# - start: Optional (defaults to 0). Inclusive.
# - stop: Required. Exclusive (The loop stops BEFORE this number).
# - step: Optional (defaults to 1). The increment value.
# ------------------------------------------------------------------------------

# Example 1: range(stop) - Single Argument
# Starts automatically at 0, steps by 1, and stops BEFORE 5.
print("Example 1:")
for i in range(5):
    print(i)
# -> Output:
# 0
# 1
# 2
# 3
# 4

print("-" * 40)

# Example 2: range(start, stop) - Two Arguments
# Starts explicitly at 2, and stops BEFORE 7.
print("Example 2:")
for i in range(2, 7):
    print(i)
# -> Output:
# 2
# 3
# 4
# 5
# 6

print("-" * 40)

# Example 3: range(start, stop, step) - Three Arguments
# Starts at 1, goes up to 10, skipping every 2 numbers (Odd numbers).
print("Example 3:")
for i in range(1, 10, 2):
    print(i)
# -> Output:
# 1
# 3
# 5
# 7
# 9


# ------------------------------------------------------------------------------
# SECTION 2: Negative Steps & Backward Counting
# ------------------------------------------------------------------------------

# Example 4: Counting Backwards (Decrementing)
# To count down, the 'start' must be greater than 'stop', and 'step' must be negative.
print("\nExample 4:")
for i in range(5, 0, -1):
    print(i)
# -> Output:
# 5
# 4
# 3
# 2
# 1


# ------------------------------------------------------------------------------
# SECTION 3: Common Real-World Use Cases
# ------------------------------------------------------------------------------

# Example 5: Using range(len()) to loop through List indices
# Useful when you need to know or modify the index position during the loop.
fruits = ["apple", "banana", "cherry"]
print("\nExample 5:")
for i in range(len(fruits)):
    print(f"Index {i}: {fruits[i]}")
# -> Output:
# Index 0: apple
# Index 1: banana
# Index 2: cherry

print("-" * 40)

# Example 6: Converting range to a List or Tuple directly
# range() doesn't generate all numbers at once; you can force it into a sequence.
print("Example 6:")
numbers_list = list(range(10, 51, 10))
print(numbers_list)
# -> Output: [10, 20, 30, 40, 50]


# ------------------------------------------------------------------------------
# SECTION 4: Senior-Level Concept - Memory Efficiency
# ------------------------------------------------------------------------------

# Example 7: Printing the range object itself vs checking memory
# range() is an "iterable object", NOT a list. It takes the same space in memory 
# whether it contains 10 numbers or 10 million numbers!
print("\nExample 7:")
huge_range = range(1, 10000000)
print(huge_range) 
# -> Output: range(1, 10000000)

# Example 8: Checking membership with 'in' operator
# Python checks if a number is inside a range using math, making it instantly fast.
print("\nExample 8:")
print(5000 in huge_range)
# -> Output: True