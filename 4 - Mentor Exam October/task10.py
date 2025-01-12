# 10. Given an array of strings strs, group the anagrams together. You can return the
# + answer in any order.

# 10. ["eat", "tea", "tan", "ate", "nat", "bat"] -> [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']],    ["abc", "bac", "cab"] -> [['abc', 'bac', 'cab']],    ["hello", "world", "python"] -> [['hello'], ['world'], ['python']
# the words “gum” and “mug” are anagrams because they are both three-letter words and have the same letters (g, u, and m). Let's look at some more word pairings that are anagrams: “cork” and “rock”


def anagram_grouper(arr):
    anagrams = {}

    for i in arr:
        # ვასორტირებთ სტრინგებს, შემდეგ შედარებისთვის
        sorted_string = ''.join(sorted(i))

        # საწყისს სტრინგს ვაბრუბებთ შესაბამის სიაში
        if sorted_string not in anagrams:
            anagrams[sorted_string] = []
            anagrams[sorted_string].append(i)

    return list(anagrams.values())

