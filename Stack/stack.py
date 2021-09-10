"""
This file contains the implementation code for a simple first-in last-out ADT (stack) classes:
 -Regular stack class.
 - Guarded Stack class
----Attributes---
        _container: List of objects
"""
from typing import Callable


class Stack:
    """
    This class is a regular stack
    ___ Private Attributes___
            _container: List[objects]

    ___ Methods___
        constractor: intializes attributes of the stack
        is_empty: checks if this stack is empy and returns boolean values
        push: pushes the provided item to the top of the stack
        push: Removes and returns the the most recent addition to the stack
        len: Return the number of Items  in this stack.
    """

    def __init__(self) -> None:
        """
        constractor method
        """
        self._container = []

    def is_empty(self) -> bool:
        """
        checks if this stack empty and return True if it is, False otherwise

        >>> stack = Stack()
        >>> stack.is_empty()
        True
        >>> stack.push("hipo")
        >>> stack.is_empty()
        False
        """
        return self._container == []

    def push(self, item: 'object') -> None:
        """
        Pushes item to the top of the stack.

        >>> stack = Stack()
        >>> items = ["files", "Names", "Numbers", "books", "classes", 24, [35,"guy", "sky"]]
        >>> for char in items:
        ...     stack.push(char)
        >>> len(stack) == len(items)
        True
        >>> stack.is_empty()
        False
        """
        self._container.append(item)

    def __len__(self) -> int:
        """
        Returns the number of items in the stack.
        >>> stack = Stack()
        >>> len(stack)
        0
        >>> items = ["files", "Names", "Numbers", "books", "classes", 24, [35,"guy", "sky"]]
        >>> for char in items:
        ...     stack.push(char)
        >>> len(stack)
        7
        """
        return len(self._container)

    def pop(self) -> 'object':
        """
        Removes and returns the the item at the top of the stack ( the item added last)

         >>> stack = Stack()
        >>> len(stack)
        0
        >>> items = ["files", "Names", "Numbers", "books", "classes", 24, [35,"guy", "sky"]]
        >>> for char in items:
        ...     stack.push(char)
        >>> len(stack)
        7
        >>> stack.pop()
        [35, 'guy', 'sky']
        >>> len(stack)
        6
        >>> stack.pop()
        24
        >>> len(stack)
        5
        """
        return self._container.pop()


class GuardedStack(Stack):
    """
    This is a child class of Stack class. The only additional requirement is that,
    before pushing item we need to check if the item meets the excepted criterion.

    ___ Additional Attributes__
        guard: Callable which checks if items meet the required criterion before adding them to the stack
        The only method we need to implement is push method
    """

    def __init__(self, guard: Callable[['object'], bool]):
        """
        Class constractor
        """
        Stack.__init__(self)
        self.guard = guard

    def push(self, item: 'object') -> None:
        """
        Add the item to the stack if it passes the guard.

        >>> items = ["files", "Names", "Numbers", "books", "classes", 24, [35,"guy", "sky"]]
        >>> def numstr(obj):
        ...     return isinstance(obj, int) or isinstance(obj, str)
        >>> gstack = GuardedStack(numstr)
        >>> for char in items:
        ...     gstack.push(char)
        >>> len(gstack)
        6
        >>> gstack.pop()
        24
        """
        if self.guard(item):
            self._container.append(item)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
