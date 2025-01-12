# # Move the first letter of each word to the end of it, then add "ay" to
# # the end of the word. 
# # Leave punctuation marks untouched.

# def pig_latin(sentence):
#     res = ''

#     splitted = sentence.split()

#     for word in splitted:
#         res += word[1:] + word[0] + 'ay '

#     return res[:-1]

# print(pig_latin('Pig latin is cool'))


# # Test Cases:
# # 'Pig latin is cool' -> 'igPay atinlay siay oolcay'
# # 'This is my string' -> 'hisTay siay ymay tringsay'
# # "Ultima necat" -> 'ltimaUay ecatnay'
# # "Lux in tenebris lucet" -> 'uxLay niay enebristay ucetlay'
# # "Cucullus non facit monachum" -> 'ucullusCay onnay acitfay onachummay'