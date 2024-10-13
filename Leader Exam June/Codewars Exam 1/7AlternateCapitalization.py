def capitalize(s):
    list = []
    first = ''
    second = ''

    result = []

    for i in s:
        list.append(i)
    
    for index, value in enumerate(list):
        if index %2== 0:
            first += value.upper()
            second += value.lower()
        else:
            first += value.lower()
            second += value.upper()
    
    result.append(first)
    result.append(second)
    print(result)




capitalize("abcdef")