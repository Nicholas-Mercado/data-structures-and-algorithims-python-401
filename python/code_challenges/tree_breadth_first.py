
from data_structures.binary_tree import BinaryTree
from data_structures.queue import Queue


def breadth_first(tree):
    final_list = []

    if tree is None:
        return final_list

    queue = Queue()
    queue.enqueue(tree.root)

    while queue:
        pass


    return final_list
