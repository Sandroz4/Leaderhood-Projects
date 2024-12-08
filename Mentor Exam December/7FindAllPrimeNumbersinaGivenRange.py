# Task:

# Write a function that takes two integers, start and end, and returns 
# a list of all prime numbers in the range [start, end]. A prime number 
# is a number greater than 1 that has no divisors other than 1 and itself.

def primeInRange(start, end):
    primes = []

    for i in range(start, end + 1):
        # მარტივი რიცხვი უნდა იყოს 1-ზე მეტი
        if i > 1:
            is_prime = True
            # მოწმდება გამყოფები რიცხვის კვადრატის ჩათვლის
            for x in range(2, int(i ** 0.5) + 1):
                if i % x == 0:
                    is_prime = False
                    break
            # თუ ქვევით მოცემული ცვლადი გახდება ჭეშმარიტი, 
            # მარტივი რიცხვი დაემატება სიაში.
            if is_prime:
                primes.append(i)

    return primes



print(primeInRange(10, 20))


# Test Cases:
# Input: start = 10, end = 20
# Output: [11, 13, 17, 19]
# Input: start = 1, end = 10
# Output: [2, 3, 5, 7]
# Input: start = 20, end = 30
# Output: [23, 29]
# Input: start = 24, end = 25
# Output: []
# Input: start = 1, end = 1
# Output: []