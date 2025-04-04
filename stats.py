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
        sorted_char = sorted(char_count.items(), key=lambda item: item[1], reverse=True)
    return sorted_char