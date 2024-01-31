import numpy as np

"""Q1 Write a NumPy program to multiply two given arrays of same size element-by-
element."""

arr1=np.array([1,2,3])
arr2=np.array([4,5,6])

arr3=[]
for i in range(len(arr1)):
    print(arr1[i]*arr2[i])
#Printing the multipled array elements
    arr3.append(arr1[i]*arr2[i])
    
print(type(arr3))

arr4=np.array(arr3)
print(arr4)
print(type(arr4))
    
