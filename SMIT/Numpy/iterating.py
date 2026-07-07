import numpy as np

arr = np.array([1, 2, 3])

for x in arr:
  print(x)


arr2d = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr2d:
  print(x)

# If we want to iterate through all the elements of a 2-D array, we need to use nested loops.
print("Iterating through 2D array using nested loops:")
for row in arr2d:
    for x in row:
        print(x)

print("Iterating through 3D array using nested loops:")
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr3d:
  for y in x:
    for z in y:
      print(z)


# Iterating Arrays Using nditer()
# The function nditer() is a helping function that can be used from very basic 
# to very advanced iterations. It solves some basic issues which we face in iteration,
# lets go through it with examples.

# Iterating on Each Scalar Element
# In basic for loops, iterating through each scalar of an array we need to use 
# n for loops which can be difficult to write for arrays with very high dimensionality.

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("Iterating through 3D array using nditer():")
for x in np.nditer(arr): # Now we can iterate n dimensional arrays using a single for loop.
  print(x)