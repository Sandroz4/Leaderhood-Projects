# # Write a function with the rules:

# # returns true  / True if every element in an array is an 
# # integer or a float with no decimals.
# # returns true  / True if array is empty.
# # returns false / False for every other input.

# def checker(arr):
#     if not arr:
#         return False
#     elif arr:
#         return all(isinstance(x, int) or 
#         (isinstance(x, float) and x.is_integer()) for x in arr)
#     else:
#         return False


# print(checker(['3']))
# # Test cases:
# # [] -> True
# # [1, 2, 3, 4] -> True
# # [1.0, 2.0, 3.0] -> True
# # [1.0, 2.0, 3.0001] -> False
# # ["-1"] -> False

# # 