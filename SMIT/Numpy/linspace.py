import numpy as np

# np.linspace creates an array of evenly spaced numbers over a specified interval.
# Basic signature: numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
# - start: first value in the sequence
# - stop: last value in the sequence (included by default if endpoint=True)
# - num: number of samples to generate
# - endpoint: if True, stop is the last sample; if False, stop is excluded
# - retstep: if True, also return the sample spacing between values

# Example 1: 10 values from 0 to 10 (inclusive)
a = np.linspace(0, 10, 10)
print("Example 1 - 10 values from 0 to 10:", a)

# Example 2: 5 values from 0 to 1 (inclusive)
b = np.linspace(0, 1, 5)
print("Example 2 - 5 values from 0 to 1:", b)

# Example 3: exclude the endpoint (stop not included)
c = np.linspace(0, 1, 5, endpoint=False)
print("Example 3 - 5 values from 0 to 1 (endpoint=False):", c)

# Example 4: also return the step between samples using retstep=True
d, step = np.linspace(0, 2, 5, retstep=True)
print("Example 4 - values:", d)
print("Example 4 - step between samples:", step)

# Example 5: specify dtype (useful when you need a specific numeric type)
e = np.linspace(0, 1, 5, dtype=np.float32)
print("Example 5 - dtype float32:", e, "dtype:", e.dtype)

# Example 6: generating values along a specific axis in multi-dimensional arrays
# Here we create a 2x5 array where the 5 values come from linspace along axis=1
f = np.linspace(0, 1, 5)
g = np.tile(f, (2, 1))  # simple way to make a 2x5 array with repeated rows
print("Example 6 - 2x5 array made from linspace row:")
print(g)

# Notes for beginners:
# - Use linspace when you need a specific number of evenly spaced points.
# - If you instead want a specific step size, consider np.arange(start, stop, step).
# - Floating point rounding can cause the last element to be slightly different than stop.