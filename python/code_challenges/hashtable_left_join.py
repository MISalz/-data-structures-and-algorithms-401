from data_structures.hashtable import Hashtable


def left_join(table_a, table_b):
    joined_table = []
    # setting an empty list to append to

    for key, value in table_a.items():
        if table_b.get(key):
            joined_table.append([key, value, table_b.get(key)])
    # for the key and value in the first table cal the items
    # append the kaye, value, and table_b's key to the joined_table
    # continue until there is nothing left in either table
    # if key exists get the key and the value and append it

        else:
            joined_table.append([key, value, 'NONE'])
    # if else, append to the table and replace the key with None


    print(joined_table)
    return joined_table
© 2022 GitHub, Inc.
Terms
Privacy
Security
