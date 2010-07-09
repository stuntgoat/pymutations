#!/usr/bin/python

def add_at_index(new_item, target_array, target_index):
    """
    new_item is a single list item.
    target_array is a list or iterable.
    target_index is a number.

    This function returns a new list that inserts new_item inside target_array
    at target_array's target_index. The new list will be 1 element longer
    than before.
    """
    
    new_list = target_array[:]

    new_list.insert(target_index, new_item)
    return new_list


def insert_each(orphan_item, target_array):
    """
    orphan_item is a single list item.
    target_array is a list or iterable.

    This function returns a list of lists that place orphan_item in between and at 
    the ends of each list element in target_array
    """

    new_array_length = len(target_array) + 1
    array_of_arrays = []
    
    for count in range(new_array_length):
        array_of_arrays.append(add_at_index(orphan_item, target_array, count))
        
    return array_of_arrays


def append_lists(working_list, list_of_lists):
    # appends every list in list_of_lists to working_list; returns working_list
    for _list in list_of_lists:
        working_list.append(_list)
    return working_list


def permute(original_list, list_of_lists):
    """
    accept a list of items, original_list, to insert one at a time into list_of_lists
    using the function insert_each. Called for the first time,
    new_list is a list containing an empty list. Then call recursively using
    an updated list_of_lists, called new_list_of_lists below, and the remaining
    items in original list.
    """
    try:
        last_item = original_list.pop()
    except IndexError:
        # if the final iteration has been completed
        return list_of_lists
    
    if list_of_lists == [[]]: # it is the first iteration
        # call the next iteration recursively
        return permute(original_list, [[last_item]])
    else:
        # placeholder for new permutations
        new_list_of_lists = []
        for array in list_of_lists:
            permutation_set = insert_each(last_item, array)
            append_lists(new_list_of_lists, permutation_set)
    # call recursively
    return permute(original_list, new_list_of_lists)


## EXAMPLE    
# trial2 = ['best', 'words', 'believe', 'jokes', 'solution', 'work']
    
# mylist = permute(trial2, [[]])

# for item in mylist:
#     sentence = ' '.join(item)
#     print(sentence)
