from data_structures.linked_list import Node
from data_structures.invalid_operation_error import InvalidOperationError

class Stack:
    """
    Put docstring here
    """

    def __init__(self):
        self.top = None


    def push(self, value):
        self.top = Node(value, self.top)
        
