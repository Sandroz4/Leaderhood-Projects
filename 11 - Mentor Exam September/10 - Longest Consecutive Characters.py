# Write a function longest_consecutive_char(s) that 
# returns the longest run of the same character.

def longest_consecutive_char(s):
    if not s:
        return ('', 0)
    
    max_char = s[0]
    max_count = 1
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            count = 1

        # if current_count > max_count:
        #     max_count = current_count
        #     max_char = current_char
        
        if count > max_count:
            max_count = count
            max_char = s[i]
        
    return (max_char, max_count)

print(longest_consecutive_char("aaabbbaaac"))

# Test Cases:
# longest_consecutive_char("aaabbbaaac") == ("a",3)
# longest_consecutive_char("bbbbb") == ("b",5)
# longest_consecutive_char("") == ("",0)
