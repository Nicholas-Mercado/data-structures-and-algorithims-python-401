
class LinkedList:
    """
    Put docstring here
    """

    def __init__(self):
        self.head = None

    def insert(self, value):
        self.head = Node(value, self.head)

    def __str__(self):
        null = 'NULL'
        if self.head is None:
            return null
        current = self.head
        output = ''
        while current:
            output += '{ ' + current.value + ' }' + ' -> '
            current = current.next
        return output + null


    def includes(self, target_value):
        current = self.head

        while current:
            if current.value == target_value:
                return True
            current = current.next
        return False

    def append(self, data):
        new = Node(data)
        maybe_head = self.head
        while maybe_head.next is not None:
            maybe_head = maybe_head.next
        maybe_head.next = new

    def insert_after(self, target_node_value, data):
        new = Node(data)
        if self.head is None:
            return 'nope'
        current = self.head

        while current:

            if current.value == target_node_value:
                current.next = new
                break
            current = current.next

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class TargetError:
    pass


linked_list = LinkedList()

linked_list.insert("apple")

linked_list.insert("banana")

linked_list.insert_after("banana", "cucumber")




