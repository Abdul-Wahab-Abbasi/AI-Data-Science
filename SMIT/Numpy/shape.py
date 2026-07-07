import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [5, 6, 7, 8]],ndmin=5)

# print(arr)
# print(arr.shape)
# print(len(arr))

arr_n =  np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])
arr_n_2 = arr_n.reshape(6,3)
# print(arr_n_2)
# print(arr_n_2.shape)

arr_n_3 = arr_n.reshape(3,3,2)
# print(arr_n_3)
# print(arr_n_3.shape)

arr_n_4 = arr_n.reshape(3,2,1,3)
# print(arr_n_4)
# print(arr_n_4.shape)


arr_n_5 = arr_n.reshape(3,2,1,-1)
# print(arr_n_5)
# print(arr_n_5.shape)