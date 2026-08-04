# ==============================================================================
# NumPy Joining & Splitting Arrays 
# ==============================================================================

import numpy as np

# ------------------------------------------------------------------------------
# 1. Joining Arrays (concatenate, hstack, vstack)
# ------------------------------------------------------------------------------
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# 1D Concatenation
join_1d = np.concatenate((arr1, arr2))

print("1D Concatenate:", join_1d)
# Output: [1 2 3 4 5 6]

# 2D Concatenation (along rows: axis=0, along columns: axis=1)
arr2d_1 = np.array([[1, 2], [3, 4]])
arr2d_2 = np.array([[5, 6], [7, 8]])

join_rows = np.concatenate((arr2d_1, arr2d_2), axis=0)

print("\n2D Concatenate Axis 0 (Rows):\n", join_rows)
# Output:
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]

join_cols = np.concatenate((arr2d_1, arr2d_2), axis=1)

print("\n2D Concatenate Axis 1 (Columns):\n", join_cols)
# Output:
# [[1 2 5 6]
#  [3 4 7 8]]


# Stacking (hstack for horizontal)  --->(.hstack)    row
# Stacking ((vstack for vertical)  --->(.vstack)     column

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2), axis=1)

print(arr)
# Output: [[1 4]
#          [2 5]
#          [3 6]]


h_stacked = np.hstack((arr1, arr2))
v_stacked = np.vstack((arr1, arr2))

print("\nHorizontal Stack (hstack):", h_stacked)
# Output: [1 2 3 4 5 6]

print("\nVertical Stack (vstack):\n", v_stacked)
# Output:
# [[1 2 3]
#  [4 5 6]]


# Stacking Along Depth / Height    ---> (.dstack)
# np.dstack() stacks arrays along height/depth (3rd dimension - axis 2).
# It pairs corresponding elements together into 3D.

arr_d1 = np.array([1, 2, 3])
arr_d2 = np.array([4, 5, 6])

d_stacked = np.dstack((arr_d1, arr_d2))

print("\n=== Stacking Along Depth (dstack) ===")
print("Output:\n", d_stacked)
# Output:
# [[[1 4]
#   [2 5]
#   [3 6]]]

print("Shape:", d_stacked.shape)
# Output: (1, 3, 2)  ---> (1 array , 3 rows , 2 columns)


# ------------------------------------------------------------------------------
# 2. Splitting Arrays  ---> (.array_split)
# ------------------------------------------------------------------------------
arr_to_split = np.array([1, 2, 3, 4, 5, 6])

# Split 1D array into 3 equal parts
split_3 = np.array_split(arr_to_split, 3)

print("Split 1D into 3 parts:", split_3)
# Output: [array([1, 2]), array([3, 4]), array([5, 6])]

# Split 2D Array into 2 parts along rows
arr2d_to_split = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
split_2d_rows = np.array_split(arr2d_to_split, 2)


print("\nSplit 2D by rows (2 parts):\n", split_2d_rows)
# Output:
# [array([[1, 2],
#        [3, 4]]), 
#  array([[5, 6],
#        [7, 8]])]



# Split the array in 4 parts:

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 4)

print(newarr)


# Output : [array([1, 2]), array([3, 4]), array([5]), array([6])]



# Access the splitted arrays:

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)
print (newarr)
# Output : [array([1, 2]), array([3, 4]), array([5, 6])]
print(newarr[0])
print(newarr[1])
print(newarr[2])

# Output : 
#[1 2]
#[3 4]
#[5 6]


# Split the 2-D array into three 2-D arrays along columns.

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3, axis=1)

print(newarr)
#[array([[ 1],
 #      [ 4],
 #      [ 7],
 #      [10],
 #      [13],
 #      [16]]), array([[ 2],
 #      [ 5],
 #      [ 8],
 #      [11],
 #      [14],
 #     [17]]), array([[ 3],
 #      [ 6],
 #      [ 9],
 #      [12],
 #      [15],
 #      [18]])]