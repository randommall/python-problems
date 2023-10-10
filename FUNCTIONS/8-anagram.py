"""
Write a function that checks if a given string is an anagram of another string.


An anagram is a word or phrase formed by rearranging the letters of another word or phrase, using all the original letters exactly once.
"""

def is_anagram(str1, str2):
    str1_cleaned = str1.replace(" ", "").lower()
    str2_cleaned = str2.replace(" ", "").lower()

    # Check if the sorted characters of the cleaned strings are the same
    return sorted(str1_cleaned) == sorted(str2_cleaned)


word1 = "listen"
word2 = "silent"
phrase1 = "Astronomer"
phrase2 = "Moon starer"

result1 = is_anagram(word1, word2)
result2 = is_anagram(phrase1, phrase2) 

result3 = is_anagram("hello", "world") 

print(result1) 
print(result2) 
print(result3) 