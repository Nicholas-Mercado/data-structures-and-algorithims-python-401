class Hashtable:
    """
    Put docstring here
    """

    def __init__(self, size=1024):
        self.size = size

    def hash(self, key):
        hash_num = 0
        for char in key:
            hash_num += ord(char)
        prime = hash_num * 599
        return prime % self.size
