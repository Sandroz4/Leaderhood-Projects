def abbreviate(s):
    def abbreviate_word(word):
        if len(word) < 4:
            return word
        return word[0] + str(len(word) - 2) + word[-1]

    result = ""
    word = ""

    for i in s:
        if i.isalpha():
            word += i
        else:
            if word:
                result += abbreviate_word(word)
                word = ""
            result += i

    if word:
        result += abbreviate_word(word)

    return result