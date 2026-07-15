# numpy.stack() joins a sequence of arrays along a NEW axis.
# Unlike concatenate() (which joins along an existing axis and keeps the same
# number of dimensions), stack() adds one extra dimension.
# All the input arrays must have the exact same shape.

# Syntax
# numpy.stack((a1, a2, ...), axis=0)

# Parameters:
# (a1, a2, ...): A tuple/list of the arrays to join. They must all be the same shape.
# axis (optional): The position of the new axis. 0 -> stack as rows (default),
#                  1 -> stack as columns.
# Return Value: Returns a new array with one more dimension than the inputs.

import numpy as np

# Example 1: Stacking two 1D arrays -> becomes a 2D array
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
res = np.stack((a, b))
print(res)
# Output:
# [[1 2 3]
#  [4 5 6]]


# Example 2: Same arrays but stacked along axis=1 (paired as columns)
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
res = np.stack((a, b), axis=1)
print(res)
# Output:
# [[1 4]
#  [2 5]
#  [3 6]]


# numpy.vstack() is a shortcut to stack arrays vertically (row on top of row).
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
res = np.vstack((a, b))
print(res)
# Output:
# [[1 2 3]
#  [4 5 6]]


# numpy.hstack() is a shortcut to stack arrays horizontally (side by side).
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
res = np.hstack((a, b))
print(res)
# Output: [1 2 3 4 5 6]


# Quick tip:
# concatenate() -> joins along an existing axis, dimensions stay the same.
# stack()       -> creates a new axis, so the result has one extra dimension.


