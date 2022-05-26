# from data_structures.hashtable import Hashtable

import re

def first_repeated_word(str):
    lower_string = (str).lower()
    lower_string = lower_string.strip()
    lower_string = re.sub(r'\n', '', lower_string)
    keys = lower_string.split(' ')
    stripped_words = []

    for word in keys:
        text = re.sub(r"[!?',;.]", '', word)
        stripped_words.append(text)

    word_dict = dict.fromkeys(stripped_words, 0)

    for word in stripped_words:
        word_dict[word] = word_dict.get(word, 0) + 1
        if word and word_dict[word] == 2:
            return word

    return




