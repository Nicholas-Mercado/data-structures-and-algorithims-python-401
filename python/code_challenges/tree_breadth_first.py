
from data_structures.binary_tree import BinaryTree
from data_structures.queue import Queue


def breadth_first(tree):
    final_list = []
    if tree is None:
        return final_list

    queue = Queue()

    if tree.root:
        queue.enqueue(tree.root)

    while queue.front:
        temp_node = queue.dequeue()
        final_list.append(temp_node.value)

        if temp_node.left is not None:
            queue.enqueue(temp_node.left)
            
        if temp_node.right is not None:
            queue.enqueue(temp_node.right)

    return final_list
