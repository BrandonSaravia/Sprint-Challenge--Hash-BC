#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """

    for i in range(length):
        hash_table_insert(ht, weights[i], i)
        
    for i in range(length):

        needed_weight = limit - weights[i]
        weight1 = hash_table_retrieve(ht, needed_weight)

        if weight1 != None and weights[weight1] + weights[i] == limit:
            if weight1 >= i:
                solution = (weight1, i)
                return solution
            else:
                solution = (i, weight1)
                return solution
    
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
