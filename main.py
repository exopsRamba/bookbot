import sys
from stats import get_num_words
from stats import get_char_count
from stats import sort_char_dict

def get_book_text(path):
    file_content = None
    with open(path) as f:
        file_content = f.read()
    return file_content

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    
    book_text = get_book_text(sys.argv[1])
    print('----------- Word Count ----------')
    print(f'Found {get_num_words(book_text)} total words')
    print('--------- Character Count -------')
    char_list = sort_char_dict(get_char_count(book_text))
    for char in char_list:
        print(f'{char["char"]}: {char["num"]}')
    return None

main()