from data_structures.queue import Queue
from data_structures.kary_tree import KaryTree, Node

def fizz_buzz_tree(tree):

    queue = Queue()
    fizz_buzz_tree = KaryTree(tree.root)
    queue.enqueue(tree.root)

    while not queue.is_empty():

        node = queue.dequeue()

        node.value = is_fizz_buzz(node.value)
        for child in node.children:
            queue.enqueue(child)

    return fizz_buzz_tree


