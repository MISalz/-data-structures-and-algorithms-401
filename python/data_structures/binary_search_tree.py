from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
    Create a Binary Search Tree class
    This class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following additional methods:
    """
    def add(self, value):
        '''
         Add
        Arguments: value
        Return: nothing
        Adds a new node with that value in the correct location in the binary search tree.
        '''
        def walk(root, new_node):
            if not root:
                return

            if new_node.value < root.value:
                if root.left:
                    walk(root.left, new_node)
                else:
                    root.left = new_node
            else:
                if root.right:
                    walk(root.right, new_node)
                else:
                    root.right = new_node

        node_to_add = Node(value)

        if not self.root:
            self.root = node_to_add
            return

        walk(self.root, node_to_add)

    def contains(self, value):
        '''
        Contains
        Argument: value
        Returns: boolean indicating whether or not the value is in the tree at least once.
        '''

        def walk(root, input_value):
            if root.value == input_value:  # found
                return True
            elif input_value > root.value and root.right is None:
                return False
            elif input_value < root.value and root.left is None:
                return False

            if root.value < input_value:
                return walk(root.right, input_value)
            elif root.value > input_value:
                return walk(root.left, input_value)

        return walk(self.root, value)


