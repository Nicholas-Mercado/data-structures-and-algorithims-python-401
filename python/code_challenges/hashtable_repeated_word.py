# from data_structures.hashtable import Hashtable
# string_1 = "Once upon a time, there was a brave princess who..."

def first_repeated_word(str):
    keys = str.split(' ')
    word_dict = dict.fromkeys(keys, 0)
    for word in keys:
        word_dict[word] = word_dict.get(word, 0) + 1
        if word_dict[word] == 2:
            return word

    print(word_dict)
    return



# first_repeated_word(string_1)

