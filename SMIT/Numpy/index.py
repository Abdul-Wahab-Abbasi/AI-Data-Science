import numpy as np

# checking version
print(np.__version__)

# creating arrays of different dimensions
zero_dimension_array = np.array(1)
one_dimension_array = np.array([1,4,7,10])
two_dimension_array = np.array([[1,4,7,10],[13,15,17,20],[13,15,17,20]])
three_dimension_array = np.array([[[1,4,7,10],[13,15,17,20],[13,15,17,20]]])

# checking arrays values
print(f"Zero Dimension Array: {zero_dimension_array}")
print(f"One Dimension Array: {one_dimension_array}")
print(f"Two Dimension Array: {two_dimension_array}")
print(f"Three Dimension Array: {three_dimension_array}")

# checking types 
print(f"\nZero Dimension Array Type: {type(zero_dimension_array)}")
print(f"One Dimension Array Type: {type(one_dimension_array)}")
print(f"Two Dimension Array Type: {type(two_dimension_array)}")
print(f"Three Dimension Array Type: {type(three_dimension_array)}")

# checking dimensions
print(f"\nDimensions: {zero_dimension_array.ndim}")
print(f"Dimensions: {one_dimension_array.ndim}")
print(f"Dimensions: {two_dimension_array.ndim}")
print(f"Dimensions: {three_dimension_array.ndim}")


# An array can have any number of dimensions.
# When the array is created, you can define the number of dimensions by using the ndmin
# argument.

arr = np.array([1, 2, 3, 4], ndmin=1)
print(arr)
print('number of dimensions :', arr.ndim)


# accessing elements
# creating arrays of different dimensions
zero_dimension_array = np.array(1)
one_dimension_array = np.array([1,4,7,10])
two_dimension_array = np.array([[1,4,7,10],[13,15,17,20],[13,15,17,20]])
three_dimension_array = np.array([[[1,4,7,10],[13,15,17,20],[13,15,17,20]],[[21,24,27,30],[33,35,37,40],[43,45,47,50]]])
# 2nd element of one dimension array
print(f"Second element of one dimensional array: {one_dimension_array[1]}")
print(f"Second element of first array of two dimensional array: {two_dimension_array[0,1]}")
print(f"Second element of second array of two dimensional array: {two_dimension_array[1,1]}")
print(f"Second element of second array of third dimensional array: {three_dimension_array[1,1,1]}")


