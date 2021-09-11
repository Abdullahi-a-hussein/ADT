"""
This file contains the code for implementing ADT first=in first-out (queue) classes:
    Queue class
    PriorityQueue
I am going to use regular python list for the implementation of these queues.
"""
from typing import Callable, List


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


if __name__ == "__main__":
    import doctest
    doctest.testmod()
