from stats import get_num_words
from stats import get_num_chars
from stats import sorted_char_list

def get_book_test(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    file = "books/frankenstein.txt"
    #get_book_test(file)
    num_words = get_num_words(file)
    print(f"{num_words} words found in the document")
    sorted_char_list(file)

main()