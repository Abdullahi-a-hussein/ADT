"""
This contains Queue Class implemented with Linked list as a container.
"""
from Linkedlist import linkedlist
from queue import Queue


class LinkQueue:
    """
    this is Queue class implemented using Linkedlist
    """

    def __init__(self):
        """
        constractor method
        """
        self.container = linkedlist.LinkedList([])

    def __len__(self):
        """
        return the number of elements in this Queue
        """
        return len(self.container)

    def enqueue(self, item):
        """
        Add item to the queue
        """
        self.container.insert(0, item)

    def dequeue(self):
        """
        remove and return the earliest item that went into this list.
        """
        if len(self) > 0:
            return self.container.pop()
        else:
            raise IndexError


if __name__ == "__main__":
    import time
    lstQ = Queue()
    lnkQ = LinkQueue()
    lst = [i for i in range(1000000)]
    # enqueing timing
    start = time.time()
    for item in lst:
        lstQ.enqueue(item)
    stop = time.time()

    start1 = time.time()
    for item in lst:
        lnkQ.enqueue(item)
    stop1 = time.time()

    print("--- %s seconds ---" % (stop - start))
    print("--- %s seconds ---" % (stop1 - start1))

    start_time = time.time()
    for i in range(1000):
        lstQ.dequeue()
    stop_time = time.time()

    start_time1 = time.time()
    for i in range(1000):
        lnkQ.dequeue()
    stop_time1 = time.time()

    print("--- %s seconds ---" % (stop_time - start_time))
    print("--- %s seconds ---" % (stop_time1 - start_time1))





