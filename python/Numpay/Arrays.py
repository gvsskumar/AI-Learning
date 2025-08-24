import numpy as np

# 1. Create array from Python list
arr1 = np.array([1, 2, 3, 4, 5])
print("Array from list:", arr1)

# 2. Create array from NumPy function
arr2 = np.zeros(5)
print("Array from zeros:", arr2)

arr3 = np.ones(5)
print("Array from ones:", arr3)

arr4 = np.arange(5)
print("Array from arange:", arr4)

arr5 = np.linspace(0, 1, 5)
print("Array from linspace:", arr5)

# 3. Create 2D array (matrix)
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", arr2)

# 4. Identity matrix
identity = np.eye(4)   # 4x4 identity matrix
print("Identity matrix:\n", identity)

# 5. Reshape array
arr1 = np.array([1, 2, 3, 4, 5, 6])
reshaped = arr1.reshape(2, 3)
print("Reshaped array:\n", reshaped)

# 6. Concatenate arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
concatenated = np.concatenate((arr1, arr2))
print("Concatenated array:", concatenated)

# 7. Split array
arr1 = np.array([1, 2, 3, 4, 5, 6])
split = np.split(arr1, 2)
print("Split array:", split)

# 8. Stack arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
stacked = np.stack((arr1, arr2))
print("Stacked array:\n", stacked)

# 8. Random array
random_arr = np.random.rand(3, 3)  # 3x3 random numbers between 0–1
print("Random array:\n", random_arr)

# 9. Random integer array
random_int_arr = np.random.randint(0, 10, (3, 3))  # 3x3 random integers between 0 and 10
print("Random integer array:\n", random_int_arr)

# 10. Random normal array
random_normal_arr = np.random.randn(3, 3)  # 3x3 random numbers from a normal distribution
print("Random normal array:\n", random_normal_arr)

# 11. Random uniform array
random_uniform_arr = np.random.rand(3, 3)  # 3x3 random numbers between 0 and 1
print("Random uniform array:\n", random_uniform_arr)





