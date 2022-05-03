class LinkedList:
    """
Can successfully instantiate an empty linked list
Can properly insert into the linked list
The head property will properly point to the first node in the linked list
Can properly insert multiple nodes into the linked list
Will return true when finding a value within the linked list that exists
Will return false when searching for a value in the linked list that does not exist
Can properly return a collection of all the values that exist in the linked list
    """

    def __init__(self):
        # initialization here
        self.value = None
        self.head = None
        self.tail = None

    def __str__(self):
        string = ""
        if self.head is None:
            return 'NULL'
        current = self.head

        while current:
            string += f"{{ {current.value} }} -> "
            current = current.next
        string += 'NULL'
        return string

    def insert(self, value):
        self.head = Node(value, self.head)
        self.value = str(value)

    def includes(self, target_value):
        current = self.head
        while current:
            if current.value == target_value:
                return True
            current = current.next
        return False

    def append(self, value):
        '''
        append
        arguments: new value
        adds a new node with the given value to the end of the list
        '''
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node


    def insert_before(self, value, new_value):
        '''
           insert before
           arguments: value, new value
           adds a new node with the given new value immediately before the first node that has the value specified
           '''
        if self.head is None:
            raise TargetError
        if self.includes(value) is False:
            raise TargetError

        new_node = Node(new_value)
        current = self.head
        if current.value is value:
            new_node.next = self.head
            self.head = new_node

        while current.next is not None:
            if current.next.value is value:
                new_node.next = current.next
                current.next = new_node
                return
            else:
                current = current.next

    def insert_after(self, value, new_value):
        '''
           insert after
           arguments: value, new value
           adds a new node with the given new value immediately after the first node that has the value specified
           '''
        current = self.head
        if self.head is None:
            raise TargetError
        if self.includes(value) is False:
            raise TargetError
        while current.next is not None:
            if current.value is value:
                current.next = Node(new_value, current.next)
                break
            else:
                current = current.next



    def kth_from_end(self, k):
        '''
           kth from end
           argument: a number, k, as a parameter.
           Return the node’s value that is k places from the tail of the linked list.
           You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.
           '''
        temp = self.head

        length = 0
        while temp is not None:
            temp = temp.next
            length += 1
        if k < length:
            raise TargetError

        temp = self.head
        for i in range(0, length - k):
            temp = temp.next
            print(temp.data)


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class TargetError(Exception):
    print("That's wrong")
