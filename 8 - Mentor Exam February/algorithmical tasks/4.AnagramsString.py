# # Given a string s and a string p, return the starting indices of all anagrams of p in s.
# # Input:
# # A string s (length ≤ 10⁵).
# # A string p (length ≤ 10⁴).

# def anagram(s, p):
#     sorted = sorted(p)  
#     result = []
#     size = len(p)

#     for i in range(len(s) - size + 1):  
#         current = s[i : i + size]  

#         if sorted(current) == sorted:  
#             result.append(i)  

#     return result


# print(anagram("anam", "na"))  
# print(anagram("sandro", "ndr"))         
