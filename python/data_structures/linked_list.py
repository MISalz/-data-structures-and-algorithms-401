class LinkedList:
    """
    Put docstring here
    """

    def __init__(self):
        # initialization here
        self.value = None
        self.head = None

    def __str__(self):
        string = ""
        if self.head ==None:
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

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class TargetError:
    pass
