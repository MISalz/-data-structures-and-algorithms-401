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

    '''
    append
    arguments: new value
    adds a new node with the given value to the end of the list
    '''

    def append(self, value, new_value):
        new_node = Node(new_value)
        saved_value = self.head
        while saved_value.next is not None:
            saved_value = saved_value.next
        saved_value.next = new_node
    '''
    insert before
    arguments: value, new value
    adds a new node with the given new value immediately before the first node that has the value specified
    '''
    def insert_before(self, value, new_value):
        new_node = Node(new_value)
        saved_value = self.head
        self.head = new_node
        while self.head.next is not None:
            counter += 1

            saved_value = saved_value.next
        saved_value.next = new_node



    '''
    insert after
    arguments: value, new value
    adds a new node with the given new value immediately after the first node that has the value specified
    '''


    def insert_after(self, new_value, after):
        new_node = Node(new_value)
        if after < 1:
            return after
        elif after == 1:
            temp = self.head
            self.head = new_node
        else:
            temp = self.head
            for i in range(1, after - 1):
                if temp is None:
                    temp = temp.next
            if temp is None:
                new_node.next = temp.next
                temp.next = new_node
            else:
                return None


    '''
    kth from end
    argument: a number, k, as a parameter.
    Return the node’s value that is k places from the tail of the linked list.
    You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.
    '''


    def kth_from_end(self, k):
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
