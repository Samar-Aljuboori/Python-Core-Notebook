# ==============================================================================
# NUMPY BASICS (Creating, Indexing, Slicing, Types, Copy vs View)
# ==============================================================================
# This file covers the essential foundation of NumPy arrays (ndarray).
# ==============================================================================

import numpy as np

# ------------------------------------------------------------------------------
# 1. Getting Started & Creating Arrays (0D, 1D, 2D, 3D)
# ------------------------------------------------------------------------------
# 0-D Array (Scalar / Single Number)
arr_0d = np.array(42)

# 1-D Array (Vector / Single Row or Column)
arr_1d = np.array([1, 2, 3, 4, 5])

# 2-D Array (Matrix / Table with Rows and Columns)
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])

# Checking dimensions using .ndim    ---> Number of Dimensions(ndim)
print("=== 1. Array Dimensions ===")
print("0D Dimension:", arr_0d.ndim)
print("1D Dimension:", arr_1d.ndim)
print("2D Dimension:", arr_2d.ndim)

# Output:
# === 1. Array Dimensions ===
# 0D Dimension: 0
# 1D Dimension: 1
# 2D Dimension: 2


# ------------------------------------------------------------------------------
# 2. Array Indexing (Accessing Elements)
# ------------------------------------------------------------------------------
# 1D Indexing: Zero-based (starts at 0)
print("\n=== 2. Array Indexing ===")
print("First element of 1D:", arr_1d[0])        # Returns 1
print("Last element of 1D:", arr_1d[-1])       # Returns 5

# 2D Indexing: [row_index, column_index]
print("2D Element (Row 1, Col 2):", arr_2d[1, 2]) # Returns 6

# Output:
# === 2. Array Indexing ===
# First element of 1D: 1
# Last element of 1D: 5
# 2D Element (Row 1, Col 2): 6


# ------------------------------------------------------------------------------
# 3. Array Slicing [start:end:step]
# ------------------------------------------------------------------------------
# Note: 'end' index is EXCLUDED!
numbers = np.array([10, 20, 30, 40, 50, 60, 70])

# arr_2d = np.array([[1, 2, 3], [4, 5, 6]])

print("\n=== 3. Array Slicing ===")
print("Index 1 to 5:", numbers[1:5])          # Elements from index 1 up to 4
print("Step slicing (every 2nd):", numbers[1:6:2])

# 2D Slicing: [rows_slice, columns_slice]
# Get elements at index 1 and 2 from BOTH rows
print("2D Slice (Both rows, cols 1 to 2):\n", arr_2d[0:2, 1:3])

# Output:
# === 3. Array Slicing ===
# Index 1 to 5: [20 30 40 50]
# Step slicing (every 2nd): [20 40 60]
# 2D Slice (Both rows, cols 1 to 2):
#  [[2 3]
#   [5 6]]


# 3D Slicing: Access the third element of the second array of the first array:
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0, 1, 2])       # Output: 6

# ------------------------------------------------------------------------------

# Negative Slicing

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[-3:-1])        # Output: [5 6]


# STEP ---> [start:end:steps] : Use the step value to determine the step of the slicing
arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[::2])          # Output: [1 3 5 7]



arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0:2, 2])       # Output: [3 8]



arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0:2, 1:4])        # Output: [[2 3 4]
                            #          [7 8 9]]



# ------------------------------------------------------------------------------
# 4. Data Types (dtype) & Converting Types (astype)
# ------------------------------------------------------------------------------
# NumPy uses single-character codes to define data types quickly:
# 'i' - integer          | 'f' - float           | 'b' - boolean
# 'u' - unsigned integer | 'c' - complex float   | 'm' - timedelta
# 'M' - datetime         | 'O' - object          | 'S' - string (bytes)
# 'U' - unicode string   | 'V' - void (raw data memory)


# Example 1: Creating an array with specific type character ('f' for float)
float_arr = np.array([1, 2, 3, 4], dtype='f')
print("Float Array via 'f':", float_arr)
print("Dtype:", float_arr.dtype)

# Example 2: Converting string array of numbers to integers using 'i'
str_numbers = np.array(['10', '20', '30'])
int_numbers = str_numbers.astype('i')

print("Converted to Integers:", int_numbers)
print("New Dtype:", int_numbers.dtype)

# Output:
# Float Array via 'f': [1. 2. 3. 4.]
# Dtype: float32
# Converted to Integers: [10 20 30]
# New Dtype: int32

# ValueError: In Python ValueError is raised when the
#  type of passed argument to a function is unexpected/incorrect.
# A non integer string like 'a' can not be converted to integer (will raise an error):

arr = np.array(['a', '2', '3'], dtype='i')
# Traceback (most recent call last): File "./prog.py", line 3, in 
# ValueError: invalid literal for int() with base 10: 'a'



# Checking data type automatically assigned by NumPy
fruits_arr = np.array(["apple", "banana", "cherry"])
int_arr = np.array([1, 2, 3, 4])

print("\n=== 4. Data Types ===")
print("Integers type:", int_arr.dtype)          # int64 or int32
print("Strings type:", fruits_arr.dtype)        # <U6 (Unicode string)

# Converting data type using astype()
float_arr = int_arr.astype('f')                 # Convert int to float
print("Converted to float:", float_arr)
print("New float dtype:", float_arr.dtype)

# Output:
# === 4. Data Types ===
# Integers type: int64
# Strings type: <U6
# Converted to float: [1. 2. 3. 4.]
# New float dtype: float32


arr = np.array([1, 0, 3])

newarr = arr.astype(bool)

print(newarr)
print(newarr.dtype)        # output :[ True False True]
                           #    bool


# ------------------------------------------------------------------------------
# 5. NumPy Copy vs View (Crucial Concept!)
# ------------------------------------------------------------------------------
# COPY: Creates a new array completely independent of the original.
# VIEW: Just a view/mirror of the original array (changes affect original!).

original = np.array([10, 20, 30])

# Creating a Copy
arr_copy = original.copy()
arr_copy[0] = 999  # Modify copy

# Creating a View
arr_view = original.view()
arr_view[1] = 888  # Modify view

print("\n=== 5. Copy vs View ===")
print("Original Array:", original)   # Changed by view! [10, 888, 30]
print("Copied Array:", arr_copy)     # Independent! [999, 20, 30]
print("Viewed Array:", arr_view)     # [10, 888, 30]

# Output:
# === 5. Copy vs View ===
# Original Array: [ 10 888  30]
# Copied Array: [999  20  30]
# Viewed Array: [ 10 888  30]



# ------------------------------------------------------------------------------
# 6. Checking Ownership with .base (Copy vs View)
# ------------------------------------------------------------------------------
# The --->   .base    attribute checks if an array owns its data or refers to another array.
# - Returns None if the array OWNS its data (e.g., a Copy).
# - Returns the original array if it's just a VIEW.

arr_base_test = np.array([1, 2, 3, 4, 5])

x = arr_base_test.copy()     # ---> None
y = arr_base_test.view()     # Original Array

print("\n=== Checking Data Ownership (.base) ===")
print("Copy base (owns data):", x.base)  # Returns None
print("View base (refers to original):", y.base)  # Returns [1 2 3 4 5]

# Output:
# === Checking Data Ownership (.base) ===
# Copy base (owns data): None
# View base (refers to original): [1 2 3 4 5]