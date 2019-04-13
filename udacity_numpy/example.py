import numpy as np

# Change False to True for each block of code to see what it does

# Using index arrays
if True:
    a = np.array([1, 2, 3, 4])
    b = np.array([True, True, False, False])

    print(a[b])
    print(a[np.array([True, False, True, False])])

# Creating the index array using vectorized operations
if True:
    a = np.array([1, 2, 3, 2, 1])
    b = (a >= 2)

    print(a[b])
    print(a[a >= 2])

# Creating the index array using vectorized operations on another array
if True:
    a = np.array([1, 2, 3, 4, 5])
    b = np.array([1, 2, 3, 2, 1])

    print(b == 2)
    print(a[b == 2])

    print(True + True)

