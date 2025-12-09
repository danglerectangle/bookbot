words_to_count = []
chars_to_count = []
chars_count_dict = {}
test_list_words = ["HELLO", "world"]

def get_num_words(book_text):
    words_to_count = book_text.split()
    
    print(f"Found {len(words_to_count)} total words")

def get_num_char(book_text):
    for word in book_text:
        for i in word:
            lower_char = str.lower(i)
            chars_to_count.append(lower_char)
    
    for i in chars_to_count:
        chars_count_dict[i] = 0

    for i in chars_to_count:
        chars_count_dict[i] += 1

    print(chars_count_dict)