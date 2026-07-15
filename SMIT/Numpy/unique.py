# numpy.unique() finds the unique elements of an array. 
# It is often used in data analysis to eliminate duplicate values and 
# return only the distinct values in sorted order.

# Syntax
# numpy.unique(ar, return_index=False, return_inverse=False, return_counts=False, axis=None)

# Parameters:
# ar: Input array flattened if not 1-D unless axis is specified.
# return_index: If True, returns indices of first occurrences of unique values.
# return_inverse: If True, returns indices to reconstruct the original array.
# return_counts: If True, returns the count of each unique value.
# axis: Operates along the given axis and if None, the array is flattened.

import numpy as np
a = np.array([1, 2, 2, 3, 4, 4, 4])
res = np.unique(a)
# print(res)

# lets try 2d array
a = np.array([[1, 2, 0, 3, 4, 4, 4, 5],[1, 2, 0, 3, 4, 4, 4, 5]])
res = np.unique(a)
# print(res)



# we use the return_counts=True parameter to get both the unique elements and 
# how many times each value appears in the array.

a = np.array([1, 2, 2, 3, 3, 4, 5])

res, counts = np.unique(a, return_counts=True)
# print("Unique:", res)
# print("Counts:", counts)