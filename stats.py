def get_num_words(text):
    return len(text.split())

def get_char_count(text):
    chars = {}
    for char in set(text.lower()):
        chars[char] = text.lower().count(char)
    return chars

def sort_on(items):
    return items["num"]

def sort_char_dict(dict):
    dict_list = []
    for entry in dict:
        dict_list.append({"char": entry, "num": dict[entry]})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
