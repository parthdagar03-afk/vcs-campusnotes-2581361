print("Parth Dagar URN:258361")
import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([1, 2, 3, 4, 5, 6])

print("Array 1:", arr1)
print("Array 2:", arr2)

print("\nSlicing:")
print("arr1[1:4]:", arr1[1:4])

print("\nSplitting:")
split_arr1 = np.split(arr1, 3)
print("Split arr1 into 3 parts:", split_arr1)

print("\nReshaping:")
reshaped_arr1 = arr1.reshape(2, 3)
print("Reshaped arr1 (2x3):\n", reshaped_arr1)

print("\nDimensions:")
print("Shape of arr1:", arr1.shape)
print("Dimension of arr1:", arr1.ndim)

print("\nElement-wise Operations:")
print("Addition:", arr1 + arr2)
print("Subtraction:", arr1 - arr2)
print("Multiplication:", arr1 * arr2)
print("Division:", arr1 / arr2)

list1 = arr1.tolist()
list2 = arr2.tolist()

print("\nConverted to Lists:")
print("List 1:", list1)
print("List 2:", list2)

concat_arr = np.concatenate((arr1, arr2))
print("\nConcatenated Array:", concat_arr)

rev_arr1 = arr1[::-1]
rev_arr2 = arr2[::-1]

print("Reversed arr1:", rev_arr1)
print("Reversed arr2:", rev_arr2)
