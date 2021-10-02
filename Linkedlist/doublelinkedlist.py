"""
This file contains implementation code for doubly linked list.
"""
from typing import Optional, List


class _DoubleNode:
    """
    This is a node for doubly linked list
    """

    def __init__(self, value: 'object') -> None:
        """
        constructor for doubly node
        """
        self.data, self.next, self.prev = value, None, None


class DoubleLinkedList:
    """
    This is a class for doubly linked list
    """

    def __init__(self, items: List[Optional['object']]) -> None:
        """
        constructor method to initialize properties of this linked list
        """
        if not items:
            self._first = None
        else:
            self._first = _DoubleNode(items[0])
            prev, curr = None, self._first
            for item in items[1:]:
                curr.next = _DoubleNode(item)
                prev, curr = curr, curr.next
                prev.next, curr.prev = curr, prev

    def __len__(self) -> int:
        """
        Return the number items in this linked list
        >>> obj1 = [1, 10, 2, 57, 23, 100, 83]
        >>> obj2 = [50]
        >>> obj3 = [34, 81]
        >>> link1 = DoubleLinkedList(obj1)
        >>> link2 = DoubleLinkedList(obj2)
        >>> link3 = DoubleLinkedList(obj3)
        >>> link4 = DoubleLinkedList([])
        >>> len(link3)
        2
        >>> len(link2)
        1
        >>> len(link1)
        7
        >>> len(link4)
        0
        """
        count, current = 0, self._first
        while current:
            count += 1
            current = current.next
        return count

    def __str__(self) -> str:
        """
        Return The string representation of this doubly linked list
        >>> obj1 = [1, 10, 2, 57, 23, 100, 83]
        >>> obj2 = [50]
        >>> obj3 = [34, 81]
        >>> link1 = DoubleLinkedList(obj1)
        >>> link2 = DoubleLinkedList(obj2)
        >>> link3 = DoubleLinkedList(obj3)
        >>> link4 = DoubleLinkedList([])
        >>> str(link3)
        '34 <-> 81'
        >>> str(link1)
        '1 <-> 10 <-> 2 <-> 57 <-> 23 <-> 100 <-> 83'
        >>> str(link4)
        ''
        >>> str(link2)
        '50'
        """
        holder = ""
        curr = self._first
        if curr:
            holder += str(curr.data)
        while curr:
            curr = curr.next
            if curr:
                holder += " <-> " + str(curr.data)
        return holder

# TODO: complete there rest of methods
    def insert(self, index: int, value: 'object') -> None:
        """
        >>> obj1 = [1, 10, 2, 57, 23, 100, 83]
        >>> obj2 = [50]
        >>> obj3 = [34, 81]
        >>> link1 = DoubleLinkedList(obj1)
        >>> link2 = DoubleLinkedList(obj2)
        >>> link3 = DoubleLinkedList(obj3)
        >>> link4 = DoubleLinkedList([])
        >>> link1.insert(1, 234)
        >>> str(link1)
        '1 <-> 234 <-> 10 <-> 2 <-> 57 <-> 23 <-> 100 <-> 83'
        >>> link2.insert(0, 40)
        >>> str(link2)
        '40 <-> 50'
        >>> link3.insert(50, 34)
        >>> str(link3)
        '34 <-> 81 <-> 34'
        >>> link3.insert(2, 2000)
        >>> str(link3)
        '34 <-> 81 <-> 2000 <-> 34'
        >>> link4.insert(4, 40)
        >>> str(link4)
        '40'
        """
        if not self._first:
            self._first = _DoubleNode(value)
        else:
            new_node = _DoubleNode(value)
            curr = self._first
            if index == 0:
                new_node.next = curr
                curr.prev = new_node
                self._first = new_node
            elif len(self) <= index:
                while curr.next:
                    curr = curr.next
                new_node.prev, curr.next = curr, new_node
            else:
                count = 0
                while count < index:
                    count += 1
                    curr = curr.next
                curr.prev.next = new_node
                new_node.prev = curr.prev
                new_node.next = curr
                curr.prev = new_node

    def __contains__(self, item):
        """
        Return if list contain <item>. Return False otherwise.
        """
        cur = self._first
        while cur:
            if cur.data == item:
                return True
            cur = cur.next
        return False

    def remove(self, item:'object') -> None:
        """
        Remove <item> from this linked list. Raise ValueError if Item not in list:
        >>> obj1 = [1, 10, 2, 57, 23, 100, 83]
        >>> obj2 = [50]
        >>> obj3 = [34, 81]
        >>> link1 = DoubleLinkedList(obj1)
        >>> link2 = DoubleLinkedList(obj2)
        >>> link3 = DoubleLinkedList(obj3)
        >>> link4 = DoubleLinkedList([])
        >>> link1.remove(57)
        >>> str(link1)
        '1 <-> 10 <-> 2 <-> 23 <-> 100 <-> 83'
        >>> link2.remove(50)
        >>> str(link2)
        ''
        >>> link2.remove(40)
        Traceback (most recent call last):
        ValueError
        >>> link3.remove(34)
        >>> str(link3)
        '81'
        """
        # when item not in least
        if not (item in self):
            raise ValueError
        # when Item is the first element of this list
        elif self._first.data == item:
            self._first = self._first.next
            if len(self) > 0:
                self._first.prev = None
        else:
            prev, curr = None, self._first
            while curr.data != item:
                nxt = curr.next
                prev, curr = curr, nxt
            prev.next = curr.next
            if curr:
                curr.next.prev = prev

    def pop(self) -> 'object':
        """
        remove and return the last last element in this linked list

         >>> obj1 = [1, 10, 2, 57, 23, 100, 83]
        >>> obj2 = [50]
        >>> obj3 = [34, 81]
        >>> link1 = DoubleLinkedList(obj1)
        >>> link2 = DoubleLinkedList(obj2)
        >>> link3 = DoubleLinkedList(obj3)
        >>> link4 = DoubleLinkedList([])
        >>> link1.pop()
        83
        >>> link2.pop()
        50
        >>> str(link1)
        '1 <-> 10 <-> 2 <-> 57 <-> 23 <-> 100'
        >>> str(link2)
        ''
        """
        if not self._first:
            raise IndexError
        elif len(self) == 1:
            placeholder = self._first.data
            self._first = None
            return placeholder
        else:
            prev, curr, placeholder = None, self._first, self._first.next
            while placeholder:
                prev, curr, placeholder = curr, placeholder, placeholder.next
            prev.next = placeholder
            return curr.data

    def append(self, item: 'object') -> None:
        """
        Append Item to this linked list
        >>> obj1 = [1, 10, 2, 57, 23, 100, 83]
        >>> obj2 = [50]
        >>> obj3 = [34, 81]
        >>> link1 = DoubleLinkedList(obj1)
        >>> link2 = DoubleLinkedList(obj2)
        >>> link3 = DoubleLinkedList(obj3)
        >>> link4 = DoubleLinkedList([])
        >>> link1.append(350)
        >>> str(link1)
        '1 <-> 10 <-> 2 <-> 57 <-> 23 <-> 100 <-> 83 <-> 350'
        >>> link2.append(70)
        >>> str(link2)
        '50 <-> 70'
        >>> link4.append(7)
        >>> str(link4)
        '7'
        """
        new_node = _DoubleNode(item)
        if len(self) == 0:
            self._first = new_node
        else:
            prev, curr = None, self._first
            while curr:
                nxt = curr.next
                prev, curr = curr, nxt
            prev.next = new_node
            new_node.prev = prev


if __name__ == "__main__":
    import doctest
    doctest.testmod()
