from data_structures.queue import Queue
from data_structures.linked_list import Node

class AnimalShelter:
    '''
    Create a class called AnimalShelter which holds only dogs and cats.
    The shelter operates using a first-in, first-out approach.
    '''

    def __init__(self):
        # initialization here
        self.cat_queue = Queue()
        self.dog_queue = Queue()


    def enqueue(self, animal):
        '''
        enqueue
        Arguments: animal
        animal can be either a dog or a cat object.
        '''

        if isinstance(animal, Dog):
            self.dog_queue.enqueue(animal)
        if isinstance(animal, Cat):
            self.cat_queue.enqueue(animal)


    def dequeue(self, pref):
        '''
        dequeue
        Arguments: pref
        pref can be either "dog" or "cat"
        Return: either a dog or a cat, based on preference.
        If pref is not "dog" or "cat" then return null.
        '''
        if pref is 'dog':
            return self.dog_queue.dequeue()
        if pref is 'cat':
            return self.cat_queue.dequeue()
        if pref != 'dog' and pref != 'cat':
            return None

class Dog:
    pass


class Cat:
    pass
