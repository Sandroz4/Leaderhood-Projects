# Given a list of N integers, find the smallest missing positive integer.
# Input: A list of integers arr.
# Output: Return the first missing positive integer.

def first_missing_positive(arr):
    unique_nums = set(arr)
    i = 1
    while i in unique_nums:
        i += 1
    return i 

print(first_missing_positive([1,2,3,4,5]))
print(first_missing_positive([1,2,3,4,5]))