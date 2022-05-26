# from data_structures.hashtable import Hashtable
# string_1 = "apple banana BANANA apple"


def first_repeated_word(str):
    lower_string = (str).lower()
    keys = lower_string.split(' ')
    word_dict = dict.fromkeys(keys, 0)
    for word in keys:
        # print(word)
        word_dict[word] = word_dict.get(word, 0) + 1
        if word_dict[word] == 2:
            return word

    # print(word_dict)
    return



# first_repeated_word(string_1)

