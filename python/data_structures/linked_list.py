
class LinkedList:
    """
    Put docstring here
    """

    def __init__(self):
        self.head = None
        # self.tail = None

    def insert(self, value):
        current = self.head
        self.head = Node(value, current)


    def __str__(self):
        null = 'NULL'
        if self.head is None:
            return null
        current = self.head
        output = ''
        while current:
            output += '{ ' + str(current.value) + ' }' + ' -> '
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
        current = self.head
        if current is None:
            current = new
            return
        else:
            while current.next is not None:
                current = current.next
            current.next = new


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
            else:
                current = current.next

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
