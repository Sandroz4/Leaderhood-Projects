def dig_pow(n, p):
    sum = 0
    num_str = str(n)
    
    for i, digit in enumerate(num_str):
        sum += int(digit)**(p+i)
    
#     if sum %n == 0:
#         return sum/n
#     else:
#         return -1
    return sum/n if sum%n == 0 else -11 