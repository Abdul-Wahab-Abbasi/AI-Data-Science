# numpy.concatenate() joins two or more arrays together into a single array.
# It is used when you want to combine arrays end-to-end (or along a chosen axis).
# The arrays must have the same shape, except in the direction you are joining.

# Syntax
# numpy.concatenate((a1, a2, ...), axis=0)

# Parameters:
# (a1, a2, ...): A tuple/list of the arrays you want to join. Note the double brackets.
# axis (optional): The direction to join along. 0 -> join rows (stack vertically, default),
#                  1 -> join columns (stack side by side). Use None to flatten then join.
# Return Value: Returns a new array with all the values joined together.

import numpy as np

# Example 1: Joining two simple 1D arrays
arr_1 = np.array([1, 2, 3, 4])
arr_2 = np.array([5, 6, 7, 8])
res = np.concatenate((arr_1, arr_2))
print(res)
# Output: [1 2 3 4 5 6 7 8]


# Example 2: Joining three arrays at once
a = np.array([1, 2])
b = np.array([3, 4])
c = np.array([5, 6])
res = np.concatenate((a, b, c))
print(res)
# Output: [1 2 3 4 5 6]


# Example 3: 2D arrays joined along axis=0 (rows added below each other)
a = np.array([[1, 2],
              [3, 4]])
b = np.array([[5, 6],
              [7, 8]])
res = np.concatenate((a, b), axis=0)
print(res)
# Output:
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]


# Example 4: 2D arrays joined along axis=1 (columns added side by side)
a = np.array([[1, 2],
              [3, 4]])
b = np.array([[5, 6],
              [7, 8]])
res = np.concatenate((a, b), axis=1)
print(res)
# Output:
# [[1 2 5 6]
#  [3 4 7 8]]
