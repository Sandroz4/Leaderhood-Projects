# 6. Given two sorted arrays nums1 and nums2, return the mean of the two sorted arrays.

# 6. [1, 2, 3], [4, 5, 6] -> 3.5,    [10, 20], [30, 40, 50] -> 30.0,    [-5, -3, -1], [1, 3, 5] -> 0.0

def mean_of_sorted(a, b):
    joined = a + b

    # საშუალო არითმეტიკულის დათვლის ფორმულა
    return (sum(joined) / len(joined))


