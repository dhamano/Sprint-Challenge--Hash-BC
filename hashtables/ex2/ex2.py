#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)

    """
    YOUR CODE HERE
    """
    for i in range(0, length):
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)
    
    flight = []
    source = "NONE"
    next = "NONE"
    for i in range (0, length):
        source = next
        next = hash_table_retrieve(hashtable, source)
        flight.append(next)

    return flight

