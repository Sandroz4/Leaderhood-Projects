# 1️⃣3️⃣ Maximum Product Subarray
# Instructions:

#  Find the contiguous subarray within an array 
#  which has the largest product.

def max_product(arr):
    if len(arr) == 0:
        return 0
    
    max_product = arr[0]

    for i in range(len(arr)):
        current_product = 1
        for x in range(i, len(arr)):
            current_product *= arr[x]

            if current_product > max_product:
                max_product = current_product
    return max_product


print(max_product([-2,0,-1]))




# Test Cases:
# [2,3,-2,4] → 6
# [-2,0,-1] → 0
# [0,-3,1,-2] → 1
