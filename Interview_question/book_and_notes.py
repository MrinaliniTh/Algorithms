def can_create_notes_from_book(book, notes):
    book_dict = {}
    for ch in book:
        if ch in book_dict:
            book_dict[ch] += 1
        else:
            book_dict[ch] = 1
    for ch in notes:
        if ch in book_dict:
            book_dict[ch] -= 1
            if book_dict[ch] < 0:
                return False
        else:
            return False
    return True

print(can_create_notes_from_book("this is a book of english", "english is best"))