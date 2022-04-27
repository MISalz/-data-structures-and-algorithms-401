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

    def append(self, new_value):
        app_node = Node(new_value)
        if self.head is None:
            self.head = app_node
            return
        else:
            prev_node = self.head
            while prev_node.next is None:
                prev_node = prev_node.next
        # prev_node = app_node

    '''
    insert before
    arguments: value, new value
    adds a new node with the given new value immediately before the first node that has the value specified
    '''

    def insert_before(self, new_value):
        new_node = Node(new_value)
        new_node.next = self.head
        self.head = new_node

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


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# class TargetError(self):
#     if self.head is None:
#         raise TargetError
#     if self.includes(value) is False:
#         raise TargetError
