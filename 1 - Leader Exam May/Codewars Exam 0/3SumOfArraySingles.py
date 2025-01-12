def repeats(arr):
    dict = {}

    for i in arr:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    
    unique_nums = []
    for num, count in dict.items():
        if count == 1:
            unique_nums.append(num)

    return sum(unique_nums)