# 1. Given an array containing n-1 numbers taken from the range 1 to n, write a 
# function to find the missing number. There are no duplicates in the array.

# 1. [1, 2, 4, 5] -> 3, [1] -> 2, [2, 3, 1, 5] -> 4

def missing_number(arr):
    # გვჭირდება სიის სიგრძეზე ერთით მეტი რიცხვი
    n = len(arr) + 1

    # წესით ჯამი უნდა იყოს ამ ფორმულის შედეგი
    expected = n * (n + 1) //2 

    current = sum(arr)

    # დაკარგული რიცხვი გამოდის მოსალოდნელ ჯამს გამოკლებული რეალური
    number = expected - current

    return number

