from stats import get_num_words, get_chars_count

def get_book_text(filepath):
    book_text = ""
    with open(filepath) as f:
        book_text = f.read()
    return book_text

def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = get_num_words(book_text)
    print(f"{word_count} words found in the document")
    print(get_chars_count(book_text))

main()