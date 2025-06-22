# 🔟 Count Inversions in an Array
# Instructions:

#  An inversion is a pair (i,j) such that i < j and
#  arr[i] > arr[j]. Write a function to count the 
# number of inversions in an array using modified merge sort.


def inversion_count(arr):
    result = 0

    for i in range(len(arr)):
        for x in range(i, len(arr)):
            if arr[i] > arr[x]:
                result += 1
    return result 

print(inversion_count([3,2,1]))


# Test Cases:
# [1,20,6,4,5] → 5
#  Inversions: (20,6), (20,4), (20,5), (6,4), (6,5)
# [2,4,1,3,5] → 3
#  Inversions: (2,1), (4,1), (4,3)
# [1,2,3] → 0
#  Array sorted ascending, no inversions.
# [3,2,1] → 3
#  Inversions: (3,2), (3,1), (2,1)
