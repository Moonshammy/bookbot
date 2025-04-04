from stats import get_num_words
from stats import get_num_chars
import sys

def get_book_test(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def print_report(chars, words, file):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for key, value in chars:
        char = str(key)
        if char.isalpha():
            print(f"{key}: {value}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file = sys.argv[1]
    char_count = get_num_chars(file)
    words = get_num_words(file)
    print_report(char_count, words, file)


main()