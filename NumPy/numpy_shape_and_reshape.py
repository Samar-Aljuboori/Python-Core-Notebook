# ==============================================================================
# NUMPY SHAPE & RESHAPING
# ==============================================================================
# This file covers how to inspect array dimensions (.shape) and how to 
# restructure arrays into different dimensions (.reshape).
# ==============================================================================

import numpy as np

# ------------------------------------------------------------------------------
# 1. Inspecting Array Shape (.shape)
# ------------------------------------------------------------------------------
# The    .shape    attribute returns a tuple of integers indicating the size of each dimension.

arr_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print("=== 1. Checking Array Shape ===")
print("Array:\n", arr_2d)
print("Shape:", arr_2d.shape)  # Output: (2, 4) -> 2 rows, 4 columns

# 3D Array Example
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("3D Array Shape:", arr_3d.shape)  # Output: (2, 2, 2)


# ------------------------------------------------------------------------------
# 2. Reshaping Arrays (.reshape)
# ------------------------------------------------------------------------------
# Reshaping allows us to add or remove dimensions, or change the number of elements per dimension.
# Rule: Total elements MUST remain the same (e.g., 12 elements -> 3x4, 2x6, 4x3, 2x2x3).

arr_1d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# Reshape from 1D (12 elements) to 2D (4 rows, 3 columns)
arr_2d_reshaped = arr_1d.reshape(4, 3)

# Reshape from 1D (12 elements) to 3D (2 matrices, 3 rows, 2 columns)
arr_3d_reshaped = arr_1d.reshape(2, 3, 2)

print("\n=== 2. Reshaping Arrays ===")
print("Original 1D:\n", arr_1d)
print("Reshaped to 2D (4, 3):\n", arr_2d_reshaped)
print("Reshaped to 3D (2, 3, 2):\n", arr_3d_reshaped)


# ------------------------------------------------------------------------------
# 3. Unknown Dimension (-1 Trick)
# ------------------------------------------------------------------------------
# You are allowed to pass -1 for ONE dimension.
# NumPy will automatically calculate the missing dimension size for you!

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# Example 1: Set rows to 2, let NumPy calculate columns (-1)
# .reshape(number_of_rows, -1) ---> -1 auto-calculates columns!
auto_cols = arr.reshape(2, -1)   # (2 rows, -1 columns) 

# Example 2: Reverse case: Set columns to 2, let NumPy calculate rows (-1)
# .reshape(-1, number_of_columns) ---> -1 auto-calculates rows!
auto_rows = arr.reshape(-1, 2)    # (-1 rows, 2 columns) 


print("\n=== 3. Reshape with Unknown Dimension (-1) ===")
print("Auto-calculated Columns Shape (2, -1):\n", auto_cols)  # Shape: (2, 4)
print("Auto-calculated Rows Shape (-1, 2):\n", auto_rows)     # Shape: (4, 2)


# Convert 1D array (8 elements) to 3D array with shape (2, 2, -1)
# NumPy calculates the missing 3rd dimension: 8 / (2 * 2) = 2

arr_3d_auto = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr_3d = arr_3d_auto.reshape(2, 2, -1)

print("\n=== 3D Reshape with Unknown Dimension (-1) ===")
print("Calculated Shape:", newarr_3d.shape)  # Output: (2, 2, 2)
print("Array Output:\n", newarr_3d)

# -----------------------------------------------------------------------------
# 4. Flattening Arrays (Converting Multidimensional Array to 1D)
# ------------------------------------------------------------------------------
# Flattening means converting any n-dimensional array into a simple 1D array.

arr_multi = np.array([[1, 2, 3], [4, 5, 6]])
flattened = arr_multi.reshape(-1)

print("\n=== 4. Flattening Arrays ===")
print("Flattened 1D Array:", flattened)  # Output: [1 2 3 4 5 6]


# ------------------------------------------------------------------------------
# 6. Advanced ndmin Example (8D Array with 5 elements)
# ------------------------------------------------------------------------------
# In this example, the original vector has 5 elements [1, 2, 3, 4, 9].
# Setting ndmin=8 forces NumPy to create an 8-dimensional array.
# It adds 7 outer dimensions of size 1, keeping the 5 elements in the last dimension.

arr_8d = np.array([1, 2, 3, 4, 9], ndmin=8)

print("\n=== 6. Advanced ndmin Example ===")
print("8D Array Output:\n", arr_8d)
print("Shape of Array:", arr_8d.shape)          # Output: (1, 1, 1, 1, 1, 1, 1, 5)
print("Total Dimensions (.ndim):", arr_8d.ndim)  # Output: 8
print("Last Dimension Size:", arr_8d.shape[-1])  # Output: 5

# Output:
# === 6. Advanced ndmin Example ===
# 8D Array Output:
#  [[[[[[[[1 2 3 4 9]]]]]]]]
# Shape of Array: (1, 1, 1, 1, 1, 1, 1, 5)
# Total Dimensions (.ndim): 8
# Last Dimension Size: 5


# ------------------------------------------------------------------------------
# 7. Reshaping Constraint (Can We Reshape Into Any Shape?)
# ------------------------------------------------------------------------------
# NO! Reshaping is only possible if the total number of elements matches.
# Formula: Product of dimensions in new shape MUST equal the original array length.
#
# Valid example: 8 elements ---> 2x4 = 8 elements (Allowed)
# Invalid example: 8 elements ---> 3x3 = 9 elements (Raises ValueError)

arr_8 = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# Trying to reshape 8 elements into shape (3, 3) which needs 9 elements:
try:
    invalid_reshape = arr_8.reshape(3, 3)
except ValueError as e:
    print("\n=== 7. Reshaping Error Example ===")
    print("Error caught successfully!")
    print("Error Message:", e)

# Output:
# === 7. Reshaping Error Example ===
# Error caught successfully!
# Error Message: cannot reshape array of size 8 into shape (3,3)


# ------------------------------------------------------------------------------
# 8. Does Reshape Return a Copy or a View?
# ------------------------------------------------------------------------------
# .reshape() typically returns a VIEW, meaning it shares the same memory.
# We can check this using the `.base` attribute:
# - If `.base` returns the original array ---> It is a VIEW.
# - If `.base` returns None ---> It is a COPY.

arr_base = np.array([1, 2, 3, 4, 5, 6, 7, 8])

reshaped_view = arr_base.reshape(2, 4)

print("\n=== 8. Checking Copy vs View in Reshape ===")
print("reshaped_view.base output:")
print(reshaped_view.base)  # Output: [1 2 3 4 5 6 7 8] (Proves it's a VIEW!)