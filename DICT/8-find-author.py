"""
Given a dictionary of book titles and their authors, find the author of a specific book.

"""

# Sample dictionary of book titles and their authors
book_authors = {
    'The Great Gatsby': 'F. Scott Fitzgerald',
    'To Kill a Mockingbird': 'Harper Lee',
    '1984': 'George Orwell',
    'Pride and Prejudice': 'Jane Austen',
    'The Catcher in the Rye': 'J.D. Salinger'
}

# Book title to look up
book_to_lookup = '1984'

# Check if the book title exists in the dictionary and get its author
if book_to_lookup in book_authors:
    author = book_authors[book_to_lookup]
    print(f"The author of '{book_to_lookup}' is: {author}")
else:
    print(f"'{book_to_lookup}' is not found in the dictionary.")
