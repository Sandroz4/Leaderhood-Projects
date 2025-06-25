# 1️⃣ Sum Digits Until Single Digit
# Instructions:

# Write a function that takes a non-negative integer and 
# returns the sum of its digits. If the result has more than 
# one digit, repeat the process until the result is a single digit.

def sum_until(num):
    num_str = str(num)

    while len(num_str) > 1:
        result = 0 

        for i in num_str:
            result += int(i)
        num_str = str(result)
    return int(num_str)

print(sum_until(0))



# Test Cases:
# 123 → 6
# 0 → 0
# 9999 → 9
# 45 → 9
# 1 → 1
