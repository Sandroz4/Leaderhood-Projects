# 2️⃣ Convert a List to a Dictionary
# Instructions:

#  Write a function that converts a list of key-value pair tuples 
# into a dictionary.

def list_dicter(tuple):
    result = {}

    for i in tuple:
        key = i[0]
        value = i[1]

        result[key] = value

    return result

print(list_dicter([('one', 1), ('two', 2)]))

# Test Cases:
# [('a', 1), ('b', 2)] → {'a': 1, 'b': 2}
# [] → {}
# [('x', 10)] → {'x': 10}
# [('a', 1), ('a', 2)] → {'a': 2}
# [('one', 1), ('two', 2)] → {'one': 1, 'two': 2}
