#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(length)

    """
    YOUR CODE HERE
    """
    if length < 2:
        return None

    for i in range(0, length):
        hash_table_insert(ht, weights[i], i)
        # print(ht.storage)
    
    keep_going = True
    i = 0
    while i < length:
        val_to_find = limit - weights[i]
        check_find = hash_table_retrieve(ht, val_to_find)
        # print(f"check_find: {check_find} | val_to_find: {val_to_find}")
        if check_find is not None:
            if check_find < i:
                return [i, check_find]
            else:
                return [check_find, i]
        else:
            i += 1


    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

# print(get_indices_of_item_weights([9,1],2,10))
# print(get_indices_of_item_weights([4, 6, 10, 15, 16],5,21))
# print(get_indices_of_item_weights([4,4],2,8))
# print(get_indices_of_item_weights([12, 6, 7, 14, 19, 3, 0, 25, 40],9,7))