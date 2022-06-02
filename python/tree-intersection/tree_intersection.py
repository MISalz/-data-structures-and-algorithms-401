from data_structures.binary_tree import BinaryTree
from data_structures.hashtable import Hashtable


def tree_intersection(tree1, tree2):

    common_values = set()

    ht = Hashtable()

    tree_1_values= tree1.pre_order()
    tree_2_values= tree2.pre_order()

    for value in tree_1_values:

        ht.set(str(value), value)

    for value in tree_2_values:

        if ht.contains(str(value)):
            
            common_values.add(value)

    return common_values
