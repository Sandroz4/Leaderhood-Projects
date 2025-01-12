# # 2. Write a function to find the longest common prefix among an array of strings.
# #  If there is no common prefix, return an empty string.


# # 2. ["flower", "flow", "flight"] -> "fl", ["dog", "racecar", "car"] -> "", 
# # ["apple", "apple", "apple"] -> "apple"

# def common_prefix(arr):
#     if not arr:
#         return ""
    
#     #პირველი სიტყვა
#     prefix = arr[0]

#     # მეორე სიტყვიდან ვუვლით სიას
#     for i in arr[1:]:
#         # თუ იტერაციაში მყოფი სიტყვა არ იწყება პრეფიქსით, ვამოკლებთ მას
#         while not i.startswith(prefix):
#             prefix = prefix[:-1]

#         if not prefix:
#             return ""
#     return prefix



