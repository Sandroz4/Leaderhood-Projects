# დავალებაში მოცემულია 5 ნორმალური სირთულის და 5 რთული დონის ალგორითმული ამოცანა.
# თითოეულ ამოცანას გააჩნია თავისი პირობა და 3 test case.

# თითოეული ამოცანისთვის უნდა შექმნათ ცალკე პითონის ან js-ის (ამ ორი ენიდან, რომლითაც გინდათ დაწერეთ ამოცანის კოდი) ფაილი და სამივე test case-ზე მიიღოთ იგივე შედეგი.
# შესაძლოა ამოცანამ მოცემულ 3 test case-ზე იგივე შედეგი დააბრუნოს, მაგრამ სხვა მაგალითებზე სწორად არ მუშაობდეს. ასეთ დროს ის შესრულებულად არ ჩაითვლება.

# !!! ყველა ამოცანას უნდა ქონდეს კომენტარები, სადაც ახსნილი იქნება კოდის რა ნაწილი რა დავალებას ასრულებს.

# !!! ამოცანების შესრულებისას დაუშვებელია browser-ის გამოყენება.


# ამოცანები:

# 1. Given an array containing n-1 numbers taken from the range 1 to n, write a 
# function to find the missing number. There are no duplicates in the array.

# 2. Write a function to find the longest common prefix among an array of strings.
#  If there is no common prefix, return an empty string.

# 3. Given an array of size n, find the majority element. The majority element is 
# the element that appears more than n // 2 times. You may assume that the array 
# is non-empty and the majority element always exists in the array.

# 4. Write a function to return the nth number in the Fibonacci sequence. Solve it 
# both recursively and iteratively.

# 5. Given an array of integers, find all unique pairs of elements that sum to a 
# given target number.

# 6. Given two sorted arrays nums1 and nums2, return the mean of the two sorted arrays.

# 7. Given a string containing just the characters '(' and ')', find the length of the
#  longest valid (well-formed) parentheses substring.

# 8. Given an array nums of n integers, return all unique triplets [a, b, c] 
# such that a + b + c = 0. The solution set must not contain duplicate triplets.

# 9. Given an array nums, return an array output such that output[i] is equal to 
# the product of all the elements of nums except nums[i].

# 10. Given an array of strings strs, group the anagrams together. You can return the
# + answer in any order.

# Test cases:
# 1. [1, 2, 4, 5] -> 3, [1] -> 2, [2, 3, 1, 5] -> 4
# 2. ["flower", "flow", "flight"] -> "fl", ["dog", "racecar", "car"] -> "", ["apple", "apple", "apple"] -> "apple"
# 3. [3, 2, 3] -> 3, [2, 2, 1, 1, 2] -> 2, [1, 1, 1, 1, 1] -> 1
# 4. 0 -> 0, 5 -> 5, 10 -> 55
# 5. [1, 2, 3, 2, 4], 5 -> [(1, 4), (2, 3)],    [1, 2, 3], 7 -> [],    [-1, 0, 1, 2, -2, 3], 0 -> [(-1, 1), (-2, 2)]
# 6. [1, 2, 3], [4, 5, 6] -> 3.5,    [10, 20], [30, 40, 50] -> 30.0,    [-5, -3, -1], [1, 3, 5] -> 0.0
# 7. "(()))())" -> 4, "((()))" -> 6, ")()())(" -> 4
# 8. [-1, 0, 1, 2, -1, -4] -> [[-1, -1, 2], [-1, 0, 1]],    [1, 2, 3] -> [],    [0, 0, 0, 0] -> [[0, 0, 0]]
# 9. [1, 2, 3, 4] -> [24, 12, 8, 6], [0, 1, 2, 3] -> [6, 0, 0, 0], [0, 0, 1] -> [0, 0, 0]
# 10. ["eat", "tea", "tan", "ate", "nat", "bat"] -> [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']],    ["abc", "bac", "cab"] -> [['abc', 'bac', 'cab']],    ["hello", "world", "python"] -> [['hello'], ['world'], ['python']
# the words “gum” and “mug” are anagrams because they are both three-letter words and have the same letters (g, u, and m). Let's look at some more word pairings that are anagrams: “cork” and “rock”