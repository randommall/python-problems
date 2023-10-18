from books_5 import books_dict

selected_book = "book1"

if selected_book in books_dict:
    book_info = books_dict[selected_book]
    print(f"Title: {book_info['title']}")
    print(f"Author: {book_info['author']}")
    print(f"Published Year: {book_info['published_year']}")
    print(f"Genre: {book_info['genre']}")
else:
    print(f"The book '{selected_book}' was not found in the dictionary.")
