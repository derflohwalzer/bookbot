def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_occurance = get_chars_count(text)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print()
    for item in chars_occurance:
        if (item['char'].isalpha()):
            print(f"The '{item['char']}' character was found {item['occurance']} times") 
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_count(text):
    chars_count = {}
    for char in text.lower():
        if char in chars_count:
            chars_count[char] += 1
        else:
            chars_count[char] = 1 

    return char_dict_list(chars_count)

def sort_on(dict):
    return dict["occurance"]

def char_dict_list(chars_count):
    chars_list = []
    for char in chars_count:
       chars_list.append({'char': char, 'occurance': chars_count[char]})

    chars_list.sort(reverse=True, key=sort_on)

    return chars_list



main()