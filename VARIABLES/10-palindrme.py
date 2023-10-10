"""Implement a program that checks if a string variable is a palindrome 
(reads the same forwards and backwards). no loop allowed. Return a true if it is a 
palindrome, otherwise false. no function, conditionals allowed

racecar
name
"""

str1 = "racecar"

str2 = "name"

rev_str1 = str1[::-1]

rev_str2 = str2[::-1]

# check palindrome
is_palindrome1 = str1 == rev_str1
is_palindrome2 = str2 == rev_str2

print("str1: ", is_palindrome1)

print("str2: ",is_palindrome2)