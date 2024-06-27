def min_sum(arr):
    arr_sum = []

    while len(arr) > 0:
        min_num = min(arr)
        max_num = max(arr)
        arr_sum.append(min_num*max_num)
        arr.remove(max_num)
        arr.remove(min_num)
    print(sum(arr_sum))

min_sum([5,4,2,3])