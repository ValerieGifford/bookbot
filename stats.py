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
