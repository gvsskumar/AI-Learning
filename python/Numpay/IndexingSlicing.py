import numpy as np

# Create 1D array
arr = np.array([10, 20, 30, 40, 50])

# Indexing
print(arr[0])   # First element → 10
print(arr[-1])  # Last element → 50

# Slicing
print(arr[1:4])   # Elements from index 1 to 3 → [20 30 40]
print(arr[:3])    # First 3 elements → [10 20 30]
print(arr[2:])    # From index 2 to end → [30 40 50]
print(arr[::2])   # Every 2nd element → [10 30 50]

# Reshaping
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d)
print(arr2d.shape)

# Indexing 2D array
print(arr2d[0, 0])  # First row, first column → 1
print(arr2d[1, 2])  # Second row, third column → 6

# Slicing 2D array
print(arr2d[:, 1])   # Second column → [2 5 8]
print(arr2d[1, :])  # Second row → [4 5 6]

# Reshaping 2D array
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr3d)
print(arr3d.shape)

# Indexing 3D array
print(arr3d[0, 0, 1])  # First 2D array, first row, second column → 2

# Slicing 3D array
print(arr3d[:, 1, :])  # Second 2D array, second row → [4 5 6]

# Reshaping 3D array
arr4d = np.array([[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]])
print(arr4d)
print(arr4d.shape)

# Indexing 4D array
print(arr4d[0, 0, 0, 1])  # First 3D array, first 2D array, first row, second column → 2

# Slicing 4D array
print(arr4d[:, 1, :, 1])  # Second 3D array, second 2D array, second row → [6 8]

# Reshaping 4D array
arr5d = np.array([[[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]], [[[17, 18], [19, 20]], [[21, 22], [23, 24]]]])
print(arr5d)
print(arr5d.shape)

# Indexing 5D array
print(arr5d[0, 0, 0, 0, 1])  # First 4D array, first 3D array, first 2D array, first row, second column → 2

# Slicing 5D array
print(arr5d[:, 1, :, 1, :])  # Second 4D array, second 3D array, second 2D array, second row → [6 8]

# Reshaping 5D array
arr6d = np.array([[[[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]], [[[17, 18], [19, 20]], [[21, 22], [23, 24]]]], [[[25, 26], [27, 28]], [[29, 30], [31, 32]]]])
print(arr6d)
print(arr6d.shape)
