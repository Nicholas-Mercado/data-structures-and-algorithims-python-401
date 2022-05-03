from distutils.log import error
from data_structures.queue import Queue


class AnimalShelter:

    def __init__(self):
        self.dog_queue = Queue()
        self.cat_queue = Queue()

    def enqueue(self, animal):
        if animal.pref == "cat":

            self.cat_queue.enqueue(animal)

        if animal.pref == "dog":

            self.dog_queue.enqueue(animal)

    def dequeue(self, pref):
        if pref == "cat":

            return self.cat_queue.dequeue()

        if pref == "dog":

            return self.dog_queue.dequeue()

        else:
            return None

class Animal():

    def __init__(self, name=None):
        self.name = name

class Dog(Animal):

    def __init__(self, name=None, pref="dog"):
        self.pref = pref

class Cat(Animal):

    def __init__(self, name=None, pref="cat"):
        self.pref = pref


# set up two queues
# dog queue, cat queue
#
