from pathlib import Path

def get_words_from_book(filename):
    try:
        # Read the file
        path = Path(f'{filename}.txt')
        contents = path.read_text()
        
        # Clean the content by replacing unwanted characters with spaces
        contents_cleaned = ''
        unwanted_chars = (',', '.', '>', '<', '”', '?', '/', '[', ']', '{', '}', '(', ')', '“', '’', '—', '‘', '~', '`', '"', '"', ';', ':', '*', '!', '@', '#', '$', '%', '^', '&', '-', '_', '|', 'TM', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
        
        for char in contents:
            if char not in unwanted_chars:
                contents_cleaned += char
            else:
                contents_cleaned += ' '
        
        # Replace newlines with spaces
        contents_cleaned = contents_cleaned.replace('\r\n', ' ')  # Windows newlines
        contents_cleaned = contents_cleaned.replace('\n', ' ')    # Unix newlines
        contents_cleaned = contents_cleaned.replace('\r', ' ')    # Old Mac newlines
        contents_cleaned = contents_cleaned.replace('\\n', ' ')   # Escaped newlines
        
        # Split into words and convert to lowercase
        words = contents_cleaned.lower().split()
        
        # Count word frequencies
        dict_count_words = {}
        for word in words:
            if word:  # Ignore empty strings
                if word in dict_count_words:
                    dict_count_words[word] += 1
                else:
                    dict_count_words[word] = 1
        
        # Sort and print the dictionary
        sort_dictionary(dict_count_words)
        
    except FileNotFoundError:
        print(f'The file {filename}.txt is not present in the current directory')

def sort_dictionary(words):
    # Sort dictionary by value (frequency) in descending order
    sorted_dict = {}
    for key in sorted(words, key=lambda k: words[k], reverse=True):
        sorted_dict[key] = words[key]  # Fixed typo: changed words[k] to words[key]
    print_a_dictionary(sorted_dict)

def print_a_dictionary(words_dict):
    for key, value in words_dict.items():
        print(f'{key} : {value}')
    print('end of program')

filename = 'moby_dick'
get_words_from_book(filename)
