from data_structures.hashtable import Hashtable


def left_join(table_a, table_b):
    '''
    CC33
    Write a function called left join
    Arguments: two hash maps
    The first parameter is a hashmap that has word strings as keys, and a synonym of the key as values.
    The second parameter is a hashmap that has word strings as keys, and antonyms of the key as values.
    Return: The returned data structure that holds the results is up to you. It doesn’t need to exactly match the output below, so long as it achieves the LEFT JOIN logic
    '''

    joined_table = []


    for key, value in table_a.items():
        if table_b.get(key):
            joined_table.append([key, value, table_b.get(key)])


        else:
            joined_table.append([key, value, 'NONE'])



    print(joined_table)
    return joined_table

