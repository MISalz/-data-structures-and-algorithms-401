from data_structures.linked_list import Node
from data_structures.invalid_operation_error import InvalidOperationError

class Stack:
    """
    Create a Stack class that has a top property. It creates an empty Stack when instantiated.
    This object should be aware of a default empty value assigned to top when the stack is created.
    """

    def __init__(self):
        # initialization here
        self.top = None

    def push(self, value):
        '''push
        Arguments: value
        adds a new node with that value to the top of the stack with an O(1) Time performance.'''
        self.top = Node(value, self.top)

    def pop(self, value):
        '''push
        Arguments: value
        adds a new node with that value to the top of the stack with an O(1) Time performance.'''
        pass

    def pop(self):
        '''pop
        Arguments: none
        Returns: the value from node from the top of the stack
        Removes the node from the top of the stack
        Should raise exception when called on empty stack'''
        if not self.top:
            raise InvalidOperationError("Method not allowed on empty collection")

        temp = self.top
        self.top = self.top.next
        return temp.value

    def peek(self):
        '''peek
        Arguments: none
        Returns: Value of the node located at the top of the stack
        Should raise exception when called on empty stack'''
        if not self.top:
            raise InvalidOperationError("Method not allowed on empty collection")

        return self.top.value

    def is_empty(self):
        '''
        is empty
        Arguments: none
        Returns: Boolean indicating whether or not the stack is empty.
        '''
        return self.top is None
