book = "books/frankenstein.txt"
book_name = "Frankenstein"


def main():
    text = get_book(book)
    w_count = word_count(text)
    print(f"{w_count} words were found in {book_name}")


def word_count(text):
    words = text.split()
    return len(words)


def get_book(file):
    with open(book) as b:
        return b.read()


main()