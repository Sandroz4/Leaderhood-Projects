# Task:

# Write a function to encrypt strings using a Caesar cipher with a given shift value.

def caesarCipher(text, shift):
    letters = "abcdefghijklmnopqrstuvwxyz"
    result = ""

    for i in text:
        # ვამოწმებთ არის თუ არა მონაცემი ანბანის ასო
        if i.isalpha():
            # გადაგვყავს პატარა ასოებში ინდექსინგის გამო
            is_upper = i.isupper()
            i = i.lower()

            # ვპოულობთ shifting-ის შედეგად მიღებულ, ახალ ინდექსს
            new_index = (letters.index(i) + shift) % len(letters)
            new_i = letters[new_index]

            # თუ თავდაპირველად პატარა ანბანური ასო იყო, 
            # ვაქცევთ ისევ დიდად.
            if is_upper:
                new_i = new_i.upper()
            result += new_i
        else:
            # თუ მონაცემი არ არის ანბანური ასო, ანუ მაგალითად არის
            # პუნქტუაცია, ემატება ჩვეულებრივ
            result += i

    return result

print(caesarCipher("Hello, World!", 5))



# Test Cases:
# Input: ("abc", 2) → Output: "cde"
# Input: ("xyz", 3) → Output: "abc"
# Input: ("Hello, World!", 5) → Output: "Mjqqt, Btwqi!"
# Input: ("Python", 0) → Output: "Python"
# Input: ("abc", -1) → Output: "zab"

