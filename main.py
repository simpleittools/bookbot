book = "books/frankenstein.txt"
book_name = "Frankenstein"


def main():
    text = get_book(book)
    w_count = word_count(text)
    print(f"{w_count} words were found in {book_name}")
    chars_dict = get_chars_dict(text)
    print(chars_dict)
    c_sorted_list = c_to_sort(chars_dict)

    print(f"--- Begin report of {book} ---")
    print(f"{word_count} words found in the document")
    print()

    for item in c_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


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


def sort_on(d):
    return d["num"]


def c_to_sort(num_c_dict):
    sorted_list = []
    for c in num_c_dict:
        sorted_list.append({"char": c, "num": num_c_dict[c]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


main()
