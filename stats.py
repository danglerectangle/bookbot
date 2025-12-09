words_to_count = [] # populated by get_num_words #
chars_to_count = [] # populated by get_num_char #
chars_count_dict = {} # populated by get_num_char #
list_of_char_dict = [] # populated by make_list_of_char_dict #
test_list_words = ["HELLO,", "world!"] # test list of strings for debugging #

def get_num_words(book_text_string): # takes book text string, converts to list of strings, prints count of string length # 
    words_to_count = book_text_string.split()
    
    print(f"Found {len(words_to_count)} total words")

def get_num_char(book_text_list): # takes list of strings, returns a dictionary: {"a": 4, "b": 23, ...} #
    for word in book_text_list:
        for i in word:
            if i.isalpha():
                lower_char = str.lower(i)
                chars_to_count.append(lower_char)
    
    for i in chars_to_count:
        chars_count_dict[i] = 0

    for i in chars_to_count:
        chars_count_dict[i] += 1
    
    return chars_count_dict

def make_list_of_char_dict(book_text_list): # takes a list of strings, makes a formatted list of dicts, then sorts them in descending "num" order and returns it: [{"char": b, "num": 23}, {"char": a, "num": 4}, ...] # 
    get_num_char(book_text_list)

    for i in chars_count_dict:
        dict_key = i
        dict_value = chars_count_dict[i]
        list_of_char_dict.append({"char": dict_key, "num": dict_value})
    
    list_of_char_dict.sort(reverse=True, key=sort_on)

    for i in list_of_char_dict:
        print(f"{i["char"]}: {i["num"]}")
    
def sort_on(list_of_dict): # sorting helper for make_list_of_char_dict #
    return list_of_dict["num"]


make_list_of_char_dict(test_list_words)