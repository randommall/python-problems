"""

Write a program that uses list comprehension to capitalize the first letter of each word in a sentence.
"""

# Input sentence
sentence = "this is a sample sentence."

# List comprehension to capitalize the first letter of each word
capitalized_words = [word.capitalize() for word in sentence.split()]

# Join the words back into a sentence
capitalized_sentence = ' '.join(capitalized_words)

# Print the result
print(capitalized_sentence)
