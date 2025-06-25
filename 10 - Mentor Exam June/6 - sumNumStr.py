# 6️⃣ Sum Numbers in a String
# Instructions:

#  Write a function that finds all numbers in a string and returns their sum.

def sum_numbers(text):
    result = 0
    current_num = ''

    for i in text:
        if i.isdigit():
            current_num = current_num + i
        else:
            if current_num != '':
                number = int(current_num)
                result += number
                current_num = ''

    # if current_num != "":
    #     number = int(current_num)
    #     result += number
    # return result 

print(sum_numbers("100 200"))


# Test Cases:
# "abc123xyz" → 123
# "7 apples and 3 oranges" → 10
# "no numbers" → 0 
# "1a2b3c" → 6
# "100 200" → 300
