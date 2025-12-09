from stats import get_num_words
from stats import get_num_char

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    get_num_words(text)
    get_num_char(text)

main()