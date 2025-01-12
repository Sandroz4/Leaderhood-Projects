# Task:

# Write a function that sums two fractions and returns the result in its simplest form. The fractions will be given as two tuples, where each tuple consists of two integers: the numerator and the denominator. To simplify the result, you need to compute the Least Common Multiple (LCM) and Greatest Common Divisor (GCD) of the denominators.
# Then, simplify the result by dividing both the numerator and denominator by their GCD.

import math

def sumFractions(frac1, frac2):
    num1, den1 = frac1
    num2, den2 = frac2

    common_den = den1 * den2

    num1 = num1 * den2
    num2 = num2 * den1
    
    
    # example of how code functions
    # 1       1        3+2    5
    # 2       3         6     6
                                    
    result_num = num1 + num2
    result_den = common_den

    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    
    greatestcd = gcd(den1, den2)
    while greatestcd != 1:
        result_num //= greatestcd
        result_den //= greatestcd
        greatestcd = gcd(result_num, result_den)


    return (result_num, result_den)

    # return result_num, result_den



print(sumFractions((2, 5), (1, 5)))


# Test Cases:
# Input: frac1 = (1, 2), frac2 = (1, 3)
# Output: (5, 6)
# Explanation: The LCM of 2 and 3 is 6. The sum is (1 * 3) / 6 + (1 * 2) / 6 = 3/6 + 2/6 = 5/6.
# Input: frac1 = (1, 4), frac2 = (1, 4)
# Output: (1, 2)
# Explanation: The LCM of 4 and 4 is 4. The sum is (1/4 + 1/4) = 2/4 = 1/2.
# Input: frac1 = (2, 5), frac2 = (1, 5)
# Output: (3, 5)
# Explanation: The LCM of 5 and 5 is 5. The sum is (2/5 + 1/5) = 3/5.
# Input: frac1 = (3, 4), frac2 = (5, 6)
# Output: (19, 12)
# Explanation: The LCM of 4 and 6 is 12. The sum is (3 * 3) / 12 + (5 * 2) / 12 = 9/12 + 10/12 = 19/12.
# Input: frac1 = (5, 12), frac2 = (7, 15)
# Output: (139, 60)
# Explanation: The LCM of 12 and 15 is 60. The sum is (5 * 5) / 60 + (7 * 4) / 60 = 25/60 + 28/60 = 53/60.
# To calculate the Greatest Common Divisor (GCD) of two numbers in Python, you can use the Euclidean algorithm, which is an efficient way to find the GCD. Here's an explanation of how to build the GCD function and how the algorithm works:
# Understanding the Euclidean Algorithm
# The Euclidean algorithm finds the GCD of two integers a and b by repeatedly applying the following steps:
# Divide a by b and calculate the remainder (a % b).
# Replace a with b and b with the remainder from the previous step.
# Repeat the process until the remainder becomes 0. The GCD will be the last non-zero value of b.
# Steps to Build GCD Function in Python
# Initial Check: If b becomes 0, then a is the GCD.
# Iterate: Continue the division and remainder operation until the remainder becomes 0.
# Understanding and Building LCM (Least Common Multiple) in Python
# The Least Common Multiple (LCM) of two integers is the smallest positive integer that is divisible by both numbers. The relationship between the LCM and GCD of two numbers can be used to efficiently compute the LCM.
# LCM(a, b) = |a * b| / GCD(a, b)
