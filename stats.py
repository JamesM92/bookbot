def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def get_num_words(string):
    words = string.split()
    num_words = len(words)
    #print(f"{num_words} words found in the document")
    return num_words

def get_num_char(string):
    #print(string)
    string = string.lower()
    chars = list(string)
    #print(chars)
    num_char = {}
    for char in chars:
        #print(char)
        if char in num_char:
            num_char[char] += 1
        else:
            num_char[char] = 1
    #print(num_char)
    return num_char

def sort_on(dict_list):
    return dict_list["num"]

def sort_dict(char_dict):
    index = 0
    dual_dict_char = []
    for char in char_dict:
        num = char_dict[char]
        dual_dict_char.append({"char":char,"num":num})
        index += 1
    dual_dict_char.sort(reverse=True, key=sort_on)
    #print(dual_dict_char)
    return dual_dict_char
