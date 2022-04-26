
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
        print(output + null)
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

    def insert_before(self, target_value, new_data):
        current = self.head
        if self.includes(target_value) is False:
            raise TargetError

        while current:
            if current.value == target_value:
                self.insert(new_data)
                break
            if current.next.value == target_value:
                current.next = Node(new_data, current.next)
                break


    def insert_after(self, target_value, new_data):
        if self.includes(target_value) is False:
            raise TargetError

        current = self.head
        while current:
            if current.value == target_value:
                current.next = Node(new_data, current.next)
                break
            current = current.next


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class TargetError(Exception):
    pass
