"""
Given a dictionary of words and their meanings, look up the meaning of a specific word.

"""

# Sample dictionary of words and their meanings
word_meanings = {
    'apple': 'a fruit with a red or green skin and white flesh that is sweet or sour to taste',
    'banana': 'a long curved fruit with a soft flesh that is yellow when ripe',
    'chocolate': 'a sweet brown food that is made from cocoa beans',
    'elephant': 'a very large animal with thick grey skin, large ears, and a long trunk',
    'computer': 'an electronic device for storing and processing data'
}

# Word to look up
word_to_lookup = 'banana'

# Check if the word exists in the dictionary and get its meaning
if word_to_lookup in word_meanings:
    meaning = word_meanings[word_to_lookup]
    print(f"The meaning of '{word_to_lookup}' is: {meaning}")
else:
    print(f"'{word_to_lookup}' is not found in the dictionary.")