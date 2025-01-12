# # You will be given a number and you will need to
# #  return it as a string in Expanded Form

# def expanded_form(number):
#     number_str = str(number)
#     length = len(number_str)
#     expanded = []

#     for value, index in enumerate(number_str):
#         if index != '0':
#             power = length - value - 1


#         expanded.append(index + '0' * power)
#     return ' + '.join(expanded)

# print(expanded_form(42))




# # Test Cases:
# # 70304 -> '70000 + 300 + 4'
# # 42 -> '40 + 2'
# # 710163 -> '700000 + 10000 + 100 + 60 + 3'
# # 853546 -> '800000 + 50000 + 3000 + 500 + 40 + 6'
# # 511604 -> '500000 + 10000 + 1000 + 600 + 4' 