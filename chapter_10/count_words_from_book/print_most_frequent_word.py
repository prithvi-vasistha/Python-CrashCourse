from pathlib import Path

def count_freq_words(words):
    dict_count_words = {}
    for word in words:
        if dict_count_words.get(word):
            dict_count_words[word] += 1
        else:
            dict_count_words[word] = 1

    return dict_count_words


def sort_dictionary(words):
    sorted_dict = {}
    for key in sorted(words, key=lambda k: words[k], reverse=True):
        sorted_dict[key] = words[key]  # Fixed typo: changed words[k] to words[key]
    
    return sorted_dict

def print_a_dictionary(words_dict):
    for key in words_dict:
       print(f'{key} : {words_dict[key]}')

    print('end of program')

def get_words_from_book(filename):
    try:
        path = Path(f'{filename}.txt')
        contents = path.read_text()
        contents = contents.strip(',.><?/[]{}()~`"";:*!@#$%^&-_|')
        contents = contents.strip("''")
        contents_cleaned = ''

        waste_content = (',','.','>','<','”','?','/','[',']','{','}','(',')','“','’','—','‘','~','`','"','"',';',':','*','!','@','#','$','%','^','&','-','_','|','™','1','2','3','4','5','6','7','8','9','0')

        for i in contents:
            if i not in waste_content:
                contents_cleaned += i
            else:
                contents_cleaned += ''

        contents_cleaned = contents_cleaned.replace('\r\n', ' ')  # Windows newlines
        contents_cleaned = contents_cleaned.replace('\n', ' ')    # Unix newlines
        contents_cleaned = contents_cleaned.replace('\r', ' ')    # Old Mac newlines
        
        words = contents_cleaned.lower().split(' ')
        #words = set(words)

        #print(words)

        #for word in words:
            #dict_count_words[word] = contents.count(word)
#
        #for word in words:
            #if dict_count_words.get(word):
                #dict_count_words[word] += 1
#
            #else:
                #dict_count_words[word] = 1

        #sort_dictionary(dict_count_words)
        dict_to_print = count_freq_words(words)
        dict_to_print = sort_dictionary(dict_to_print)
        #print_a_dictionary(dict_to_print)
        #print(dict_to_print)
        print("The top 5 most used words in moby dick are:")
        for key, value in list(dict_to_print.items()) [:5]:
            print(f'{key} : {value}')
#
    except FileNotFoundError:
        print(f'The file {filename} is not present at the current directory')


filename = 'moby_dick'
get_words_from_book(filename)
