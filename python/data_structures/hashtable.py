from data_structures.linked_list import LinkedList

class Hashtable:
    """
    Put docstring here
    """

    def __init__(self, size=1024):
        self.size = size
        self.buckets = [None] * self.size

    def hash(self, key):
        hash_num = 0
        for char in key:
            hash_num += ord(char)
        prime = hash_num * 599
        return prime % self.size

    def set(self, key, val):
        index = self.hash(key)

        bucket = self.buckets[index]

        if bucket is None:
            bucket = LinkedList()
            self.buckets[index] = bucket

        bucket.insert((key, val))

