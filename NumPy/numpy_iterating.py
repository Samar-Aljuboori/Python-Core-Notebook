import numpy as np

# ==============================================================================
# NumPy Array Iterating (التكرار على عناصر المصفوفات)
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Basic Iteration using For Loop
# ------------------------------------------------------------------------------
arr_1d = np.array([1, 2, 3])
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])

print("=== 1D Array Iteration ===")
for x in arr_1d:
    print(x)
# Output: 1, 2, 3

print("\n=== 2D Array Iteration (Iterates through rows) ===")
for row in arr_2d:
    print(row)
# Output: [1 2 3], [4 5 6]

print("\n=== 2D Array Iteration (Nested loop for scalars) ===")
for row in arr_2d:
    for item in row:
        print(item)
# Output: 1, 2, 3, 4, 5, 6

# ------------------------------------------------------------------------------
# 2. Advanced Iteration using np.nditer()
# ------------------------------------------------------------------------------
# np.nditer() iterates through every single scalar element regardless of dimension.

arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print("\n=== 3D Array Iteration using np.nditer() ===")
for x in np.nditer(arr_3d):
    print(x)
# Output: 1, 2, 3, 4, 5, 6, 7, 8

# ------------------------------------------------------------------------------
# 3. Enumerated Iteration using np.ndenumerate()
# ------------------------------------------------------------------------------
# np.ndenumerate() returns both the index position and the element value.

print("\n=== Enumerated Iteration using np.ndenumerate() ===")
for index, value in np.ndenumerate(arr_2d):
    print(f"Index: {index}, Value: {value}")
# Output:
# Index: (0, 0), Value: 1
# Index: (0, 1), Value: 2
# Index: (0, 2), Value: 3
# Index: (1, 0), Value: 4 ...

# ==============================================================================
# Summary & Notes:
# - Basic 'for' loops iterate over the first dimension (rows in 2D arrays).
# - np.nditer(): Efficient helper to visit every scalar element in n-dimensions.
# - np.ndenumerate(): Returns (index_tuple, value) for element tracking.
# ==============================================================================