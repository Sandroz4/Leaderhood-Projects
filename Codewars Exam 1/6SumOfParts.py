def parts_sums(ls):
    sum_ls = sum(ls)
    res = [sum_ls]
    
    for i in ls:
        sum_ls = sum_ls - i
        res.append(sum_ls)
    return res