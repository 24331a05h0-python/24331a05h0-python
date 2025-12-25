import numpy as np

arr = np.array([5, 10, 15, 20, 25])

print("Array:", arr)
print("Dimension:", arr.ndim)
print("Size:", arr.size)
print("Data type:", arr.dtype)
print("Sum:", np.sum(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
print("Average:", np.mean(arr))
print("Standard deviation:", np.std(arr))
print("Cumulative sum:", np.cumsum(arr))
print("Sorted array:", np.sort(arr))
print("Unique elements:", np.unique(arr))
print("Index of maximum:", np.argmax(arr))
print("Index of minimum:", np.argmin(arr))
