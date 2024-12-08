# Task:

# Write a function that generates the Xbonacci sequence. The Xbonacci sequence is a generalization of the 
# Fibonacci sequence, where each number is the sum of the previous X numbers in the sequence.
# For example, if X = 3 and the initial sequence is [1, 1, 1], the sequence will proceed as follows:
# The 4th number is the sum of the previous 3: 1 + 1 + 1 = 3.
# The 5th number is the sum of the previous 3: 1 + 1 + 3 = 5.
# The 6th number is the sum of the previous 3: 1 + 3 + 5 = 9.
# Your function should take two arguments:
# X: The number of previous terms to sum.
# n: The number of terms to generate.


def xBonacci(X, n):
    # თანმიმდევრობას ვიწყებთ x ცალი 1-იანით
    starting = [1] * X

    # აქ ვინახავთ პირველი x რიცხვით ჯამს კონკრეტულ მომენტში
    current_sum = sum(starting)

    # თანმიმდევრობაში ვამატებთ ახალ რიცხვებს
    for i in range(X, n):
        # ამ მომენტში არსებულ ჯამს ვამატებთ მომდევნო რიცხვად
        starting.append(current_sum)
        # ახლანდელ ჯამს ვაკლებთ იმ რიცხვს, რომელიც არ გვჭირდება
        # და ვამატებთ ახალს.
        current_sum += starting[-1] - starting[i - X]

    # თანმიმდევრობაში ვამატებთ პირველ n რიცხვებს
    return starting[:n]


print(xBonacci(2, 10))

# Test Cases:
# Input: X = 3, n = 10
# Output: [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]
# Explanation: The first 10 numbers of the Xbonacci sequence starting with [1, 1, 1] and X = 3.
# Input: X = 2, n = 10
# Output: [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# Explanation: This is the Fibonacci sequence, where each number is the sum of the previous two numbers.
# Input: X = 4, n = 6
# Output: [1, 1, 1, 1, 4, 7]
# Explanation: Starting with [1, 1, 1, 1], the next terms are calculated by summing the last 4 terms.
# Input: X = 5, n = 8
# Output: [1, 1, 1, 1, 1, 5, 9, 17]
# Explanation: The sequence starts with five 1s, and each subsequent number is the sum of the previous 5 numbers.
# Input: X = 3, n = 1
# Output: [1]
# Explanation: Only one term in the sequence is required, so the output is [1].
