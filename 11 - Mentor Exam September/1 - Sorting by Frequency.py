# Write a function sort_by_frequency(lst) that returns the 
# list sorted by frequency of elements (most frequent first). 
# If two numbers have the same frequency, keep the smaller 
# number first.

# def sort_by_frequency(lst):
#     counts = {}

#     for i in lst:
#         counts[i] = counts.get(i, 0) + 1
    
#     return sorted(lst, 
#     key=lambda x:(-counts[x], x))





# print(sort_by_frequency([4,4,1,2,2,3,3,3]))



# Test Cases:
# sort_by_frequency([4,4,1,2,2,3,3,3]) == [3,3,3,2,2,4,4,1]
# sort_by_frequency([10,20,10,30,20,10]) == [10,10,10,20,20,30]
# sort_by_frequency([]) == []
