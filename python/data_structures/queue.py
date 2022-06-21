from data_structures.linked_list import Node
from data_structures.invalid_operation_error import InvalidOperationError

class Queue:
    """
    Create a Queue class that has a front property. It creates an empty Queue when instantiated.
    This object should be aware of a default empty value assigned to front when the queue is created.
    The class should contain the following methods:
    """

    def __init__(self):
        # initialization here
        self.rear = None
        self.front = None

    def enqueue(self, value):
        '''
        enqueue
        Arguments: value
        adds a new node with that value to the back of the queue with an O(1) Time performance.'''
        node = Node(value)
        if self.rear:
            self.rear.next = node

        self.rear = node
        if not self.front:
            self.front = self.rear

    def dequeue(self):
        '''
        dequeue
        Arguments: none
        Returns: the value from node from the front of the queue
        Removes the node from the front of the queue
        Should raise exception when called on empty queue
        '''
        if not self.front:
            raise InvalidOperationError

        temp = self.front
        self.front = temp.next
        temp.next = None
        return temp.value

    def peek(self):
        '''
        peek
        Arguments: none
        Returns: Value of the node located at the front of the queue
        Should raise exception when called on empty stack
        '''
        if not self.front:
            raise InvalidOperationError

        return self.front.value

    def is_empty(self):
        '''
        is empty
        Arguments: none
        Returns: Boolean indicating whether or not the queue is empty
        '''
        return not self.front



