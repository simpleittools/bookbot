book = "books/frankenstein.txt"
book_name = "Frankenstein"


def main():
    text = get_book(book)
    w_count = word_count(text)
    print(f"{w_count} words were found in {book_name}")
    chars_dict = get_chars_dict(text)
    print(chars_dict)


def word_count(text):
    words = text.split()
    return len(words)


def get_book(file):
    with open(book) as b:
        return b.read()


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars




main()
