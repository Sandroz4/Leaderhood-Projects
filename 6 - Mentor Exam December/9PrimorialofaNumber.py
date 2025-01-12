# Task:

# Write a function that calculates the primorial of a number. The primorial of a number n is the product of all prime 
# numbers less than or equal to n. For example, the primorial of 5 is the product of the primes less than or equal to 5: 2 * 3 * 5 = 30.
# Your function should take an integer n and return the primorial of that number.

def is_prime(num):
    # თუ რიცხვი ნაკლებია 1-ზე, მაშინ ის არ არის მარტივი
    if num <= 1:
        return False
    # ვამწმებთ გაყოფადობას 2-იდან კონკრეტული რიცხვის კვადრატის ჩათვლით
    for i in range(2, int(num ** 0.5) + 1):
        # თუ რიცხვი ნებისმიერ ციფრზე იყოფა, ამ შემთხვევაშიც არ არის ის მარტივი
        if num % i == 0:
            return False
    return True

def primorial(x):
    # საწყის ნამრავლად ვიღებთ 1-ს, 
    # რადგან 1-ზე გამრავლება საბოლოო შედეგს არ ცვლის
    product = 1
    # ლუპით ვუვლით ციფრებს 2-იდან (რადგან 1 არ არის მარტივი და არც განვიხილავთ) n-მდე
    for i in range(2, x + 1):
        # თუ რიცხვი მარტივია, მაშინ ნამრავლის ცვლადში არსებულ ციფრზე ვამრავლებთ, რის შედეგადაც
        # ვიღებთ საბოლოო ნამრავლს
        if is_prime(i):
            product *= i
    # ვაბრუნებთ საბოლოო ნამრავლს
    return product

print(primorial(5))

# Test Cases:
# Input: n = 5
# Output: 30
# Explanation: The prime numbers less than or equal to 5 are 2, 3, and 5. Their product is 2 * 3 * 5 = 30.
# Input: n = 10
# Output: 210
# Explanation: The prime numbers less than or equal to 10 are 2, 3, 5, and 7. Their product is 2 * 3 * 5 * 7 = 210.
# Input: n = 1
# Output: 1
# Explanation: There are no primes less than or equal to 1, so the primorial is 1 by definition.
# Input: n = 7
# Output: 210
# Explanation: The prime numbers less than or equal to 7 are 2, 3, 5, and 7. Their product is 2 * 3 * 5 * 7 = 210.
# Input: n = 11
# Output: 2310
# Explanation: The prime numbers less than or equal to 11 are 2, 3, 5, 7, and 11. Their product is 2 * 3 * 5 * 7 * 11 = 2310.