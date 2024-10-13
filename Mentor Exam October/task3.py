# 3. Given an array of size n, find the majority element. The majority element is 
# the element that appears more than n // 2 times. You may assume that the array 
# is non-empty and the majority element always exists in the array.

# 3. [3, 2, 3] -> 3, [2, 2, 1, 1, 2] -> 2, [1, 1, 1, 1, 1] -> 1

def majority_element(arr):
    count = 0
    current = None

    # ვამოწმებთ რომელი აკმაყოფილებს
    # შესაბამის პირობებს
    for i in arr:
        if count == 0:
            current = i   
        if i == current:
            count += 1 
        else:
            count -=1

    return current

