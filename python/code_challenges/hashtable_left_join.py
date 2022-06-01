from data_structures.hashtable import Hashable


def left_join(ht1, ht2):

    matrix_values = []

    ht1_keys = ht1.keys()
    # print(ht1_keys)
    for key in ht1_keys:

        key_values = []

        ht2_value = ht2.get(key)

        ht1_value = ht1.get(key)

        key_values.extend([key, ht1_value, ht2_value])

        matrix_values.append(key_values)

    print(matrix_values)
    return matrix_values
