# Given a list of N integers, find the majority element (the element that appears more than N/2 times). 
# If there is no majority element, return None.
# Input: A list of integers arr.
# Output: Return the majority element or None.

def majority_element(arr):
    element, count = None, 0
    for i in arr:
        if count == 0:
            element = i
        if i == element:
            count += 1
        else:
            count -= 1
        
    if arr.count(element) > len(arr) // 2:
        return element
    return None


print(majority_element([1, 2, 2, 3]))
print(majority_element([1, 2, 2, 2, 3]))
print(majority_element([2, 4, 4, 4, 4, 2, 2, 3]))