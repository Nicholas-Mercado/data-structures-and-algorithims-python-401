from data_structures.linked_list import Node
from data_structures.invalid_operation_error import InvalidOperationError


class Queue:
    """
    Put docstring here
    """

    def __init__(self):
        self.rear = None
        self.front = None

    def enqueue(self, value):
        new_node = Node(value)

        if self.rear:
            self.rear.next = new_node

        self.rear = new_node

        if not self.front:
            self.front = self.rear

    def dequeue(self):

        if not self.front:
            raise InvalidOperationError

        prior_front = self.front
        self.front = prior_front.next

        return prior_front.value

    def peek(self):

        if not self.front:
            raise InvalidOperationError

        return self.front.value

    def is_empty(self):
        return self.front is None
