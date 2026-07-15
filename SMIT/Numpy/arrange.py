import numpy as np 

# numpy.arange() function creates an array of evenly spaced values within a given interval. 
# It is similar to Python's built-in range() function but returns a NumPy array 
# instead of a list.

# Syntax
# numpy.arange(start, stop, step, dtype=None)

# Parameters:
# start (optional): The starting value of the sequence. Default is 0.
# stop: The endpoint of the sequence, exclusive.
# step (optional): The spacing between consecutive values. Default is 1.
# dtype (optional): The desired data type of the output array.

# Return Type: array of evenly spaced values.

a = np.arange(5 , 10)
# print(a)


sequence = np.arange(0, 1, 0.2)
print("Floating-Point Sequence:", sequence)