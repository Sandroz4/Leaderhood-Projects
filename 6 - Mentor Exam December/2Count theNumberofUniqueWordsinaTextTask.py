# Task:

# Write a function that counts the number of unique words in a string, ignoring case sensitivity
# and punctuation.

def uniqueWords(sentence):
    # მარტივი ჰენდლინგისთვის წინადადებას ვაქცევთ პატარა ასოებათ
    sentence = sentence.lower()

    punctuation = ".,!?;:()|{}[]\"'"

    # თუ პუნტქუაციის ცვლადში შენახული რომელიმე მონაცემი აღმოჩნდა
    # წინადადებაში, მას ვანაცვლებთ ცარიელი სტრინგით, (არაფრით)
    for i in punctuation:
        sentence = sentence.replace(i, "")

    
    words = sentence.split()
    # სეტად ვაქცევთ გახლეჩილ სიტყვებს
    uniqueWords = set(words)

    # ვითვლით უნიკალური სიტყვების რაოდენობას სეტში
    return len(uniqueWords)


print(uniqueWords("The quick brown fox jumps over the lazy dog"))

# Test Cases:
# 1. Input: "The quick brown fox jumps over the lazy dog" → Output: 8
# 2. Input: "Hello hello world!" → Output: 2
# 3. Input: "" → Output: 0
# 4. Input: "Python is fun. Python is cool." → Output: 5
# 5. Input: "One word" → Output: 2