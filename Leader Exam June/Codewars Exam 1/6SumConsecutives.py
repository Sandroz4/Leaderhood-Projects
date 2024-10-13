def sum_consecutives(lst):
    res = []
    last = None

    for i in lst:
        if i != last:
            res.append(i)
            last = i
        else:
            res[-1] += i
    print(res)




sum_consecutives([1, 4, 4, 4, 0, 4, 3, 3, 1])