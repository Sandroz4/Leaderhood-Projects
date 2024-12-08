# Task:

# Write a function that takes a sentence and reverses the order of its words.

def reverseOrder(text):
    # ცვლადში ვინახავთ წინადადების სიტყვებად გახლეჩილ ვარიანტს, პარალელურად კი 
    # ვაბრუნებთ მას საპირისპირო მიმართულებით
    text = text.split()[::-1]
    # დაშორების გამოყენებით ვაერთებთ გახლეჩილ, უკვე შებრუნებულ სიტყვებს
    return " ".join(text)

print(reverseOrder(" Spaces "))

# Test Cases:
# 1. Input: "Hello World" → Output: "World Hello"
# 2. Input: "Python is great" → Output: "great is Python"
# 3. Input: "a b c" → Output: "c b a"
# 4. Input: "" → Output: ""
# 5. Input: " Spaces " → Output: "Spaces"