def get_num_words(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        words = file_contents.split()
        count = len(words)
    return count

def get_num_chars(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read().lower()
        char_count = {}
        for char in file_contents:
            if char not in char_count:
                char_count[char] = 1
            else:
                value = char_count[char]
                char_count[char] = value + 1
    return char_count

def sort_on(dict):
    return dict["num"]

def sorted_char_list(path_to_file):
    char_count = get_num_chars
    char_count.sort(reverse=True, key=sort_on)
    print(char_count)
