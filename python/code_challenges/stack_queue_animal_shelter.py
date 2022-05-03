from data_structures.queue import Queue


class AnimalShelter:

    def __init__(self):
        self.dog_queue = Queue()
        self.cat_queue = Queue()

    def enqueue(self, name):
        self.cat_queue.enqueue(name)

    def dequeue(self, name):
        # if self.name == "cat":

            return self.cat_queue.dequeue()

class Dog:

    def __init__(self, name="dog"):
        self.name = name

class Cat:

    def __init__(self, name="cat"):
        self.name = name


# set up two queues
# dog queue, cat queue
#
