def main():
    book_path = "books/frankenstein.txt"
    text = get_book(book_path)
    word_count = get_word_count(text)
    chars_dict = get_chars_count(text)
    sorted_char_count = sort_chars_dict(chars_dict)

    print(f"------ Begin report of {book_path} ------")
    
    print(f"{word_count} words found in the document")
    print()

    for item in sorted_char_count:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times ")

    print("----- End report -----")


def get_book(path):
    with open(path) as f:
        return f.read()
    
def get_word_count(text):
    words = text.split()
    return len(words)

def get_chars_count(text):
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

def sort_chars_dict(chars_dict):
    sorted_list = []
    for c in chars_dict:
        sorted_list.append({"char": c, "num": chars_dict[c]})
    sorted_list.sort(reverse= True, key= sort_on)
    return sorted_list

main()