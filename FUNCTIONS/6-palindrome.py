"""
Implement a function that checks if a string is a palindrome and returns True if it is or False if it's not.
"""

def is_palindrome(string):
    check_str = string.replace(" ", "").lower()

    return check_str == check_str[::-1]

result1 = is_palindrome("racecar")
result2 = is_palindrome("manneer")

print("result1 ", result1)
print("result2 ", result2)