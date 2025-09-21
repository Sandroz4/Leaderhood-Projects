# Write a function remove_consecutive_duplicates(s) 
# that removes consecutive duplicate characters from a string.

def remove_consecutive_duplicates(s):
    result = ''
    prev = None

    for char in s:
        if char != prev:
            result += char
            prev = char
    return result
    

    
    # for index, char in enumerate(s):
    #     if not s[index + 1] == char:
    #         result += char
    # return result
            
            


print(remove_consecutive_duplicates("hellooo"))

# Test Cases:
# remove_consecutive_duplicates("aaabbcddd") == "abcd"
# remove_consecutive_duplicates("hellooo") == "helo"
# remove_consecutive_duplicates("abc") == "abc"
