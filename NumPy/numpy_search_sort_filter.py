# ==============================================================================
# NumPy Search, Sort, and Filter 
# ==============================================================================

import numpy as np

# ------------------------------------------------------------------------------
# 1. Searching Arrays (np.where & np.searchsorted)
# ------------------------------------------------------------------------------
# NumPy provides functions to search for specific elements or condition matches 
# and returns the [index] positions where those conditions are satisfied.

arr_search = np.array([1, 2, 3, 4, 5, 4, 4])

# --- A. np.where() ---
# Finds the index positions (not the actual values) that meet a given condition.

# Example 1: Find indices where elements are equal to 4
x_where = np.where(arr_search == 4)
print("=== 1. Searching Arrays ===")
print("Indices where value == 4:", x_where[0])
# Output: [3 5 6] (Value 4 appears at indices 3, 5, and 6)

# Example 2: Find indices of even numbers using a condition (num % 2 == 0)
x_even = np.where(arr_search % 2 == 0)
print("Indices of even numbers:", x_even[0])
# Output: [1 3 5 6] (Even numbers exist at indices 1, 3, 5, and 6)

# Example 3: Find the indexes where the values are odd:
arr = np.array([10, 14, 93, 41, 8, 7])

x = np.where(arr%2 == 1)

print(x)    
# Output: (array([2, 3, 5]),)


# --- B. np.searchsorted() ---
# Performs a binary search on a SORTED array to determine the correct index position
# where a specified value should be inserted to maintain sort order.

arr_sorted_base = np.array([6, 7, 8, 9])

# Example: Where should the value 7 be inserted?
x_sorted = np.searchsorted(arr_sorted_base, 7)
print("Insertion index for 7:", x_sorted)
# Output: 1 (7 is placed at index 1 to keep the array sorted)



# Search From the Right Side
# By default the left most index is returned, 
# but we can give side='right' to return the right most index instead.
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7, side='right')
print(x)
# Output: 2

# --- Additional np.searchsorted() Examples ---

arr_demo = np.array([10, 20, 30, 40])

# Example 1: Insert  single value in the middle    ---> 25
idx1 = np.searchsorted(arr_demo, 25)
print("Index to insert 25:", idx1)
# Output: 2 (25 goes between index 1 and index 2)

# Example 2: Insert multiple values      ---> [5, 35]
idx2 = np.searchsorted(arr_demo, [5, 35])
print("Indices to insert [5, 35]:", idx2)
# Output: [0 3] (5 goes at index 0, 35 goes at index 3)


# ------------------------------------------------------------------------------
# 2. Sorting Arrays (np.sort)
# ------------------------------------------------------------------------------
arr_unsorted = np.array([3, 2, 0, 1])
arr_str = np.array(['banana', 'cherry', 'apple'])
arr_2d = np.array([[3, 2, 4], [5, 0, 1]])

sorted_1d = np.sort(arr_unsorted)
sorted_str = np.sort(arr_str)
sorted_2d = np.sort(arr_2d)  # Sorts each row independently

print("\n=== 2. Sorting Arrays ===")
print("Sorted Numbers:", sorted_1d)
# Output: [0 1 2 3]

print("Sorted Strings:", sorted_str)
# Output: ['apple' 'banana' 'cherry']

print("Sorted 2D Array (Row-wise):\n", sorted_2d)
# Output:
# [[2 3 4]
#  [0 1 5]]


# Sort a boolean array:
arr = np.array([True, False, True])

print(np.sort(arr))
# Output: [False True True]


# ==============================================================================
# Summary & Notes:
# - np.where(): Returns tuple of indices where condition is True.
# - np.searchsorted(): Uses binary search to find insertion position in sorted array.
# - np.sort(): Returns a sorted copy of the array (does not modify original).
# ==============================================================================



# ------------------------------------------------------------------------------
# 3. Filtering Arrays (Boolean Indexing)
# ------------------------------------------------------------------------------
arr_filter = np.array([41, 42, 43, 44])

# Create a boolean filter condition (elements > 42)
condition = arr_filter > 42
filtered_arr = arr_filter[condition]

print("\n=== 3. Filtering Arrays ===")
print("Condition Mask:", condition)
# Output: [False False  True  True]

print("Filtered Values (> 42):", filtered_arr)
# Output: [43 44]


# --- Filtering using a Boolean List (Direct Mask) ---
arr = np.array([41, 42, 43, 44])

# Define a boolean mask (True = Keep element, False = Drop element)
filter_mask = [True, False, True, False]

# Apply mask to create new filtered array
newarr = arr[filter_mask]

print("Filtered Array using Manual Mask:", newarr)
# Output: [41 43]


# ==============================================================================
# Summary & Notes:
# Filtering in NumPy ONLY relies on Boolean values (True / False).
# 
# 1. True  -> Keeps the element at this index.
# 2. False -> Drops/Ignores the element at this index.
# 
# Whether you pass a manual list of booleans [True, False, ...] or a condition 
# like (arr > 42), NumPy creates a boolean mask to filter out the values.
# ==============================================================================




