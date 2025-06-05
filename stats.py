def get_num_words(text):
    return len(text.split())

def get_chars_count(text):
    chars_count = {}
    text = text.lower()
    for char in text:
        if not char in chars_count:
            chars_count[char] = 0
        chars_count[char] += 1
    return chars_count

def sort_chars_count(chars_count):
    sorted_list = []
    for c in chars_count:
        char_count = {
            "char": c,
            "num": chars_count[c]
        }
        sorted_list.append(char_count)

    def sort_on(dict):
        return dict["num"]

    sorted_list.sort(reverse=True,key=sort_on)
    return sorted_list