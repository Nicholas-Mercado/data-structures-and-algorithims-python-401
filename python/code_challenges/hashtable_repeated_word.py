# from data_structures.hashtable import Hashtable

import re
# string_1 = "apple? BANANA! banana, apple."


def first_repeated_word(str):
    lower_string = (str).lower()
    keys = lower_string.split(' ')
    stripped_words = []

    for word in keys:
        text = re.sub(r"[!?',;.]", '', word)
        stripped_words.append(text)

    word_dict = dict.fromkeys(stripped_words, 0)

    for word in stripped_words:
        word_dict[word] = word_dict.get(word, 0) + 1
        if word_dict[word] == 2:
            return word

    print(word_dict)
    return



# first_repeated_word(string_1)

