# Project 4 — Word Counter
# Author: your name here

sentence = input("Enter a sentence: ")
words = sentence.lower().split()

# TODO: total word count using len()
total_words = len(words)

# TODO: character count (no spaces)
# Hint: sentence.replace(" ", "") removes all spaces, then use len()
total_chars = len(sentence.replace(" ", ""))

# TODO: word frequency dictionary
frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

# TODO: print total words, total characters, then word frequency
print(f"Total words: {total_words}")
print(f"Total characters (no spaces): {total_chars}")
print(f"Word frequency: {frequency}")
