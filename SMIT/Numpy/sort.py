import numpy as np 

# numpy.sort() is used to sort the elements of a NumPy array. 
# It returns a sorted copy of the array while leaving the original array unchanged. 
# Sorting can be performed on 1D arrays as well as along specific axes of multi-dimensional 
# arrays.

# Syntax
# numpy.sort(a, axis=-1, kind=None, order=None)

# Parameters:
# a: Input array to be sorted.
# axis (optional): Axis along which sorting is performed. -1 -> Sort along the last axis (default), 0 -> Sort along columns, 1 -> Sort along rows and None -> Flatten the array before sorting.
# kind (optional): Sorting algorithm to use ('quicksort', 'mergesort', 'heapsort', 'stable').
# order (optional): Field name(s) used when sorting structured arrays.
# Return Value: Returns a sorted copy of the input array.

a = np.array([10,2,0,7,3,6,5,1,4,9,8])
r = np.sort(a)
print(r)


a = np.array([10,2,0,7,3,6,5,1,4,9,8])
r = np.argsort(a)
print(r)


# a 2D array is sorted column-wise. Each column is sorted independently from top to bottom.
a = np.array([ [13, 4],
               [3, 23],
               [5, 2] ])
r = np.sort(a, axis=0)
print(r)

# The following example sorts each row of a 2D array independently.
a = np.array([ [13, 4],
               [3, 23],
               [5, 2] ])
r = np.sort(a, axis=1)
print(r)