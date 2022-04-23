
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


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class TargetError:
    pass

# linked = LinkedList()
# linked.insert("apple")
# linked.insert("orange")
