# Splitting is the opposite of joining: it breaks one array into multiple smaller arrays.
# numpy.array_split() divides an array into the number of parts you ask for.
# It is safe even when the array can't be divided evenly (it just makes some parts
# slightly smaller). numpy.split() also exists, but it ERRORS on uneven splits.

# Syntax
# numpy.array_split(ary, indices_or_sections, axis=0)

# Parameters:
# ary: The input array you want to split.
# indices_or_sections: How many parts to split into (an integer), or a list of
#                      index positions where the cuts should be made.
# axis (optional): The direction to split along. 0 -> split rows (default),
#                  1 -> split columns.
# Return Value: A list of smaller arrays.

import numpy as np

# Example 1: Split a 1D array into 2 equal parts
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 2)
print(newarr)
# Output: [array([1, 2, 3]), array([4, 5, 6])]


# Example 2: Uneven split -> array_split still works (no error)
arr = np.array([1, 2, 3, 4, 5])
newarr = np.array_split(arr, 3)
print(newarr)
# Output: [array([1, 2]), array([3, 4]), array([5])]


# Example 3: Access one of the parts by its index, just like a normal list
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr[0])   # first part
print(newarr[1])   # second part
# Output:
# [1 2]
# [3 4]


# Example 4: Splitting a 2D array along axis=0 (splits the rows)
arr = np.array([[1, 2],
                [3, 4],
                [5, 6],
                [7, 8]])
newarr = np.array_split(arr, 2, axis=0)
print(newarr)
# Output:
# [array([[1, 2],
#         [3, 4]]),
#  array([[5, 6],
#         [7, 8]])]


# numpy.hsplit() is a shortcut to split an array into columns (horizontally).
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8]])
newarr = np.hsplit(arr, 2)
print(newarr)
# Output:
# [array([[1, 2],
#         [5, 6]]),
#  array([[3, 4],
#         [7, 8]])]
