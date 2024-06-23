def divisible_by(numbers, divisor):
    res = []

    for i in numbers:
        if i %divisor == 0:
            res.append(i)
    return res



print(divisible_by([1,2,3,4,5,6], 2))