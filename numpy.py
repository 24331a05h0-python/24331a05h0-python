import numpy as np

lst = [2, 12, 30, 4, 24]
npArr = np.array(lst)
print("Array:", npArr)
print("Dimension:", npArr.ndim)
print("Sum of elements:", np.sum(npArr))
print("Maximum Element:", np.max(npArr))
print("Minimum Element:", np.min(npArr))
print("Average of elements:", np.mean(npArr))
print("First element:", npArr[0])
print("Last element:", npArr[-1])
print("Slicing (0 to 3):", npArr[0:3])
print("Elements from start to index 2:", npArr[:3])
print("Elements from index 2 to end:", npArr[2:])
print("Every second element:", npArr[::2])
print("Reversed array:", npArr[::-1])
npArr[2] = 35
print("After modifying index 2:", npArr)
npArr[1:4] = [15, 25, 45]
print("After modifying slice 1 to 3:", npArr)
