# Task:

# Write a function that determines if two strings are anagrams of each other.

def anagramChecker(word1, word2):
    # ვასორტირებთ ორივე გადმოცემულ სიტყვას
    sorted_word1 = ''.join(sorted(word1))
    sorted_word2 = ''.join(sorted(word2))

    # თუ ორივე დასორტილი სიტყვა ზუსტად დაემთხვა ერთმანეთს
    # თანმიმდევრობით, შესაბამისად გამოდის, რომ ისინი ერთმანეთის ანაგრამები არიან
    return sorted_word1 == sorted_word2

print(anagramChecker('listen', 'silent'))

# Test Cases:
# 1. Input: ("listen", "silent") → Output: True
# 2. Input: ("triangle", "integral") → Output: True
# 3. Input: ("apple", "pale") → Output: False
# 4. Input: ("a", "a") → Output: True
# 5. Input: ("rat", "car") → Output: False