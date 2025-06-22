# 1️⃣4️⃣ Maximum XOR of Two Numbers in an Array
# Instructions:

#  Find two numbers in an array that yield the maximum XOR value.

def max_xor(arr):
    if len(arr) < 2:
        return 0
    
    max_xor = 0

    for i in range(len(arr)):
        for x in range(i + 1, len(arr)):
            xor = arr[i] ^ arr[x]
            if xor > max_xor:
                max_xor = xor
    return max_xor

print(max_xor([8, 10, 2]))

# Test Cases:
# [3, 10, 5, 25, 2, 8] → 28
#  Max XOR between 5 and 25: 5 ^ 25 = 28
# [0] → 0
#  Only one number, XOR is 0
# [2, 4] → 6
#  2 ^ 4 = 6
# [8, 10, 2] → 10
#  8 ^ 2 = 10
# [12, 15, 7, 9] → 15
#  12 ^ 3 = 15 (or 15 ^ 0)