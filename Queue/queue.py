"""
This file contains the code for implementing ADT first=in first-out (queue) classes:
    Queue class
    PriorityQueue
I am going to use regular python list for the implementation of these queues.
"""
from typing import Callable


class Queue:
    """
    This class contains first-in first-out ADT queue and its methods
    ---- Private Attributes----
        _container: List[object]

    ---- Methods ----
     constractor: initializes attributes of the class
     is_empty: checks if the queue is empty
     len: Returns the number of items in the queue
     enqueue: takes an object as an argument and inserts at the end of the queue
     dequeue: Removes the first-in item from the queue and returns it.
    """

    def __init__(self):
        """
        Initialize the attributes of this queue
        """
        self._container = []

    def __str__(self):
        """
        String Representation of this Queue
        """
        return " -> ".join([str(item) for item in self._container])

    def is_empty(self) -> bool:
        """
        return True if the queue is empty, False otherwise.

        >>> q = Queue()
        >>> q.is_empty()
        True
        >>> q.enqueue("Special needs")
        >>> q.is_empty()
        False
        """
        return self._container == []

    def __len__(self) -> int:
        """
        Return the number of items in this queue

        >>> q = Queue()
        >>> len(q)
        0
        >>> q.enqueue("Special Need")
        >>> len(q)
        1
        >>> items = ["files", "Names", "Numbers", "books", "classes", 24, [35,"guy", "sky"]]
        >>> for char in items:
        ...     q.enqueue(char)
        >>> len(q)
        8
        """
        return len(self._container)

    def enqueue(self, item: 'object') -> None:
        """
        Add <item> to the end of the queue

        >>> q = Queue()
        >>> q.enqueue("butterfly")
        >>> len(q)
        1
        >>> q.dequeue()
        'butterfly'
        """
        self._container.insert(0, item)

    def dequeue(self) -> None:
        """
        Removes and returns the first item inserted in the list.

        >>> q = Queue()
        >>> q.enqueue("butterfly")
        >>> len(q)
        1
        >>> q.dequeue()
        'butterfly'
        >>> len(q)
        0
        """
        return self._container.pop()


class PriorityQueue(Queue):
    """
    This is child class of Queue. The only difference is that new Items
    is added to the queue with priority consideration.
    """

    def __init__(self, priority: Callable[['object', 'object'], bool]):
        """
        Constractor method
        """
        Queue.__init__(self)
        self.priority = priority

    def enqueue(self, item: 'object') -> None:
        """
        Add item to the queue  using the given priority consideration

        >>> def is_greater(item1, item2):
        ...     return item1 >= item2
        >>> pq = PriorityQueue(is_greater)
        >>> pq.enqueue(27)
        >>> pq.enqueue(18)
        >>> pq.enqueue(100)
        >>> str(pq)
        '18 -> 27 -> 100'
        >>> items = [3, 2, 6, 18, 27, 50, 200]
        >>> for digit in items: pq.enqueue(digit)
        >>> str(pq)
        '2 -> 3 -> 6 -> 18 -> 18 -> 27 -> 27 -> 50 -> 100 -> 200'
        """
        if self.is_empty():
            self._container.append(item)
        else:
            index = 0
            for i in range(len(self._container)):
                if self.priority(item, self._container[i]):
                    index = i+1
            self._container.insert(index, item)



if __name__ == "__main__":
    import doctest
    doctest.testmod()
