# from data_structures.hashtable import Hashtable

import re

def first_repeated_word(str):
    # clean up string for dict keys
    lower_string = (str).lower()
    lower_string = re.sub(r'\n', '', lower_string)
    keys = lower_string.split(' ')
    stripped_words = []

    # remove special characters from each list item
    for word in keys:
        text = re.sub(r"[!?',;.]", '', word)
        stripped_words.append(text)
    # Create dict
    word_dict = dict.fromkeys(stripped_words, 0)
    # increment key values and check for value of 2
    for word in stripped_words:
        word_dict[word] = word_dict.get(word, 0) + 1
        if word and word_dict[word] == 2:
            return word

    return




