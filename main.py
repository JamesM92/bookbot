import sys
from stats import get_num_words
from stats import get_num_char
from stats import get_book_text
from stats import sort_dict



def main():
    inputs = sys.argv
    if len(inputs) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = inputs[1]
    content = get_book_text(path)
    #print(content)
    num_words = get_num_words(content)
    dict_char = get_num_char(content)

    dual_dict_char = sort_dict(dict_char)

    print(f"============ BOOKBOT ==========")
    print(f"Analyzing book found at {path}...")
    print(f" - - - - - - - - - - Word Count - - - - - - - - - - -")
    print(f"Found {num_words} total words")
    print(f" - - - - - - - - - Character Count - - - - - - - - -")
    for set in dual_dict_char:
        ch = set["char"]
        nu = set["num"]
        if ch.isalpha():
            print(f"{ch}: {nu}")
    print(f"============ END ============")



main()
