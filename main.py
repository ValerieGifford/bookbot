from stats import get_num_words, get_chars_count, sort_chars_count

def get_book_text(filepath):
    book_text = ""
    with open(filepath) as f:
        book_text = f.read()
    return book_text

def main():
    file_path = "books/frankenstein.txt"
    book_text = get_book_text(file_path)
    word_count = get_num_words(book_text)
    char_dict = sort_chars_count(get_chars_count(book_text))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for c in char_dict:
        if c["char"].isalpha():
            print(f"{c["char"]}: {c["num"]}")
    print("============= END ===============")

main()