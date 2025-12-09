from stats import get_num_words
from stats import get_num_char
from stats import make_list_of_char_dict
from stats import sort_on

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def print_report(book_path, text):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    get_num_words(text)
    print("--------- Character Count -------")
    make_list_of_char_dict(text)
    print("============= END ===============")

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print_report(book_path, text)

main()