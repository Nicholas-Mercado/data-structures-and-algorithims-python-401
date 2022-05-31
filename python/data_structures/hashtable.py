from data_structures.linked_list import LinkedList


class Hashable:
    """
    Put docstring here
    """

    def __init__(self, size=1024):
        self.size = size
        self.buckets = [None] * self.size


    def hash(self, key):
        key = str(key)
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

    def get(self, key):
        index = self.hash(key)

        bucket = self.buckets[index]

        current = bucket.head

        while current:
            pair = current.value
            current_key = pair[0]
            if current_key == key:
                return pair[1]

            current = current.next

        return None

    def contains(self, key):
        index = self.hash(key)
        bucket = self.buckets[index]

        if bucket is None:
            return False

        current = bucket.head

        while current:
            pair = current.value
            current_key = pair[0]
            if current_key == key:
                return True

            current = current.next

        return False

    def keys(self):
        all_keys = []
        for bucket in self.buckets:
            if bucket:
                def climb(bucket):

                    if not bucket.head:
                        return

                    all_keys.append(bucket.head.value[0])

                    bucket.head = bucket.head.next
                    return climb(bucket)

                climb(bucket)
        print(all_keys)
        return all_keys


