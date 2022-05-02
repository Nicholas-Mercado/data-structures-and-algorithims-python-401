from data_structures.stack import Stack


class PseudoQueue:
    def __init__(self):
        self.inbox = Stack()
        self.outbox = Stack()

    def enqueue(self, value):
        self.inbox.push(value)

    def dequeue(self):
        x = self.inbox.pop()
        self.outbox.push(x)

        return self.outbox.pop()
