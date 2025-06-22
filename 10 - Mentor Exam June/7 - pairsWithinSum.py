# 7️⃣ Find Pairs with Given Sum
# Instructions:

#  Write a function that returns all pairs of 
#  numbers from a list that add up to a given target sum.

def pairs_within(arr, target):
    pairs = []

    for i in range(len(arr)):
        for x in range(i + 1, len(arr)):
            num1 = arr[i]
            num2 = arr[x]

            if num1 + num2 == target:
                pair = (num1, num2)
                pairs.append(pair)
    return pairs


print(pairs_within([5,5,5], 10))

# Test Cases:
# [1,2,3,4], 5 → [(1,4),(2,3)]
# [0,0,1,1], 1 → [(0,1),(0,1)]
# [5,5,5], 10 → [(5,5),(5,5),(5,5)]
# [1], 2 → []
# [], 0 → []
