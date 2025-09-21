# rite a function has_subset_sum(nums, target) that 
# returns True if any subset of numbers adds up to target.

# def has_subset_sum(nums, target):
#     if target == 0:
#         return True
#     if not nums:
#         return False
    

#     return(has_subset_sum(nums[1:], target - nums[0]) or 
#            has_subset_sum(nums[1:], target))
 

# print(has_subset_sum([3,34,4,12,5,2], 9))


# Test Cases:
# has_subset_sum([3,34,4,12,5,2], 9) == True  # 4+5
# has_subset_sum([3,34,4,12,5,2], 30) == False
# has_subset_sum([], 0) == True
