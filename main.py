def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def count_words(book_text):
    words_to_count = []
    words_to_count = book_text.split()
    print(f"Found {len(words_to_count)} total words")

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count_words(text)

main()
