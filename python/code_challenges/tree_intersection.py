from data_structures.binary_tree import BinaryTree
from data_structures.hashtable import Hashable


def tree_intersection(bt1,bt2):

    intersection_values = set()

    ht = Hashable()

    bt1_values = BinaryTree.pre_order(bt1)

    bt2_values = BinaryTree.pre_order(bt2)

    for value in bt1_values:

        ht.set(value, value)

    for value in bt2_values:
        
        if ht.contains(value):

            intersection_values.add(value)

    return intersection_values
