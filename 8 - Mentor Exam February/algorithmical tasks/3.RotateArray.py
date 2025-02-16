# # Given a list arr, rotate it to the right by k steps.
# # Input:
# # A list of integers arr.
# # An integer k.
# # Output: Return the rotated array.

# def rotate_array(arr, k):
#     size = len(arr)
#     k %= size
#     # ვაბრუნებთ
#     arr.reverse()
#     # ჯერ ვაბრუნებთ k ელემენტებს
#     arr[:k] = reversed(arr[:k])
#     # შემდეგ ვაბრუნებთ დანარჩენ ელემენტებს
#     arr[k:] = reversed(arr[k:])
#     return arr

# print(rotate_array([2,3,4,5,6,7,8], 5))
# print(rotate_array([2,3,4,5,6,7,8], 2))
# print(rotate_array([2,3,4,5,6,7,8], 1))