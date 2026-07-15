# Create an array of 10 numbers.
# Create an array from 1 to 20.
# Print the shape and dimensions of the array.
# Find the sum, average, maximum and minimum.
# Take 5 numbers from the user and perform all the operations on them.

import numpy as np
arrOf10 = np.array([1,2,3,4,5,6,7,8,9,10])
print("Array of 10 numbers:", arrOf10)
print("Shape of arrOf10:", arrOf10.shape)
print("Dimensions of arrOf10:", arrOf10.ndim)
print("Sum of arrOf10:", np.sum(arrOf10))
print("Average of arrOf10: ", np.mean(arrOf10))
print("Maximum of arrOf10: ", np.max(arrOf10))
print("Minimum of arrOf10: ", np.min(arrOf10))



arrOf20 = np.array(range(1, 21))
print("\nArray from 1 to 20:", arrOf20)
print("Shape of arrOf20:", arrOf20.shape)
print("Dimensions of arrOf20:", arrOf20.ndim)
print("Sum of arrOf20:", np.sum(arrOf20))
print("Average of arrOf20: ", np.mean(arrOf20))
print("Maximum of arrOf20: ", np.max(arrOf20))
print("Minimum of arrOf20: ", np.min(arrOf20))


userArr = []
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    userArr.append(num)

userArr = np.array(userArr)
print("\nUser Input Array:", userArr)
print("Shape of userArr:", userArr.shape)
print("Dimensions of userArr:", userArr.ndim)
print("Sum of userArr:", np.sum(userArr))
print("Average of userArr: ", np.mean(userArr))
print("Maximum of userArr: ", np.max(userArr))
print("Minimum of userArr: ", np.min(userArr))