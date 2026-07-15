# Filtering in NumPy means selecting only the elements that meet a condition.
# The most common way is a "boolean mask": you write a condition on the array,
# which gives an array of True/False values, and NumPy keeps only the True ones.

# Syntax
# filtered_array = array[condition]

# How it works:
# 1. A condition like (array > 5) returns a boolean array (True/False for each element).
# 2. Putting that boolean array inside the brackets keeps only the True positions.
# Return Value: A new 1D array containing only the elements that passed the condition.

import numpy as np

# Example 1: See the boolean mask on its own
a = np.array([10, 20, 30, 40, 50])
mask = a > 25
print(mask)
# Output: [False False  True  True  True]


# Example 2: Use the mask to filter the array
a = np.array([10, 20, 30, 40, 50])
res = a[a > 25]
print(res)
# Output: [30 40 50]


# Example 3: Keep only the even numbers (using the modulo % operator)
a = np.array([1, 2, 3, 4, 5, 6, 7, 8])
res = a[a % 2 == 0]
print(res)
# Output: [2 4 6 8]


# Example 4: Combine two conditions
# Use & for AND, | for OR. Each condition MUST be wrapped in its own ( ).
a = np.array([5, 12, 18, 25, 30, 42])
res = a[(a > 10) & (a < 30)]
print(res)
# Output: [12 18 25]


# Example 5: numpy.where() returns the INDEX positions where the condition is True
a = np.array([10, 20, 30, 40, 50])
res = np.where(a > 25)
print(res)
# Output: (array([2, 3, 4]),)  -> elements at index 2, 3 and 4 passed
