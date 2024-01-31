import numpy as np

#Q2 Write a NumPy program to find the missing data in a given array.
 
# Creating a NumPy array with "nan" i.e not a number
nums = np.array([[3, 332, np.nan, 1],
                 [810, 712,np.nan, 9]])


print(" array with missing values:")
print(nums)


print("array:")
print(np.isnan(nums))

""" isnall or isnull returns a bolean values where missing values
present return true else False"""
