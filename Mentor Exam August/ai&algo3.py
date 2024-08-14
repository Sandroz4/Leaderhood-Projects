# # Write python program that will turn decimal number into binary number.

# def decimal_to_binary(decimal_number):
#     if decimal_number < 0:
#         raise ValueError('it must be positive')
#     if decimal_number == 0:
#         return '0'
    
#     binary = ''

#     while decimal_number > 0:
#         binary = str(decimal_number%2)+binary
#         decimal_number //=2
#     return binary

# print(decimal_to_binary(32))

# # Test Cases:
# # 32 -> 100000
# # 31 -> 11111
# # 8 -> 1000
