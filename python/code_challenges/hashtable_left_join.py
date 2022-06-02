from data_structures.hashtable import Hashtable


def left_join(table_a, table_b):
    joined_table = []


    for key, value in table_a.items():
        if table_b.get(key):
            joined_table.append([key, value, table_b.get(key)])


        else:
            joined_table.append([key, value, 'NONE'])



    print(joined_table)
    return joined_table

