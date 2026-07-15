import numpy as np

# np.eye creates a 2-D array with ones on a specified diagonal and zeros elsewhere.
# The basic signature is np.eye(N, M=None, k=0) where:
# - N is the number of rows
# - M is the number of columns (if None, M = N)
# - k is the index of the diagonal: 0 is the main diagonal,
#   positive k moves the diagonal up, negative k moves it down.

# Example 1: square identity-like matrix with 6 rows and 6 columns
arr = np.eye(6)
# print(arr)         # uncomment to see the array
# print(arr.shape)   # (6, 6)


# Example 2: non-square matrix with 3 rows and 6 columns
# This places ones on the main diagonal but truncates to fit 3 rows
arr = np.eye(3, 6)
# print(arr)         # uncomment to see the array
# print(arr.shape)   # (3, 6)


# Example 3: place the diagonal 3 above the main diagonal
# This will put ones shifted to the right by 3 columns
arr = np.eye(4, 6, 3)
print(arr)            # show the array for this example
print(arr.shape)      # (4, 6)


# Example 4: diagonal one below the main diagonal (k = -1)
arr = np.eye(3, 6, -1)
# print(arr)         # uncomment to see the array
# print(arr.shape)   # (3, 6)



arr_1 = np.array([[[[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]]])
arr_2 = np.array([[[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]])
arr_3 = np.array([[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]])

print(arr_1.shape,arr_2.shape,arr_3.shape)