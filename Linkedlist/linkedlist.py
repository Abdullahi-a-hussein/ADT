"""
This model is for implementation of regular linked list
"""
from typing import List, Optional


class _Node:
    """
    This is a private class used for implementation of linked list
    """

    def __init__(self, item: 'object') -> None:
        """initialize the attribute of this node"""
        self.item = item
        self.next = None


class LinkedList:
    """
    This class is for implementation of singly linked list
    For most of the methods we implement the using loops and recursion
    """

    def __init__(self, items: List[Optional['object']]) -> None:
        """
        Consstracting method for initializing attributes of this Linkedlist
        """
        if not items:
            self._first = None
        else:
            self._first = _Node(items[0])
            current_node = self._first
            for item in items[1:]:
                current_node.next = _Node(item)
                current_node = current_node.next

    def __str__(self):
        """
        String representation of this linked list

        >>> link = LinkedList([3,"item", "blue", "green"])
        >>> str(link)
        '3 -> item -> blue -> green'
        """
        required = ""
        if not self._first:
            return required
        else:
            required += str(self._first.item)
            cur_node = self._first
            while cur_node:
                cur_node = cur_node.next
                if cur_node:
                    required += " -> " + str(cur_node.item)
        return required

    def __len__(self):
        """
        Returns the number of items in this linked list

        >>> items = [2, "google", 3, "apple", 4, "Amazon", 5, "facebook"]
        >>> link = LinkedList(items)
        >>> len(link)
        8
        >>> linky = LinkedList([])
        >>> len(linky)
        0
        """
        counter, cur_node = 0, self._first
        while cur_node:
            counter += 1
            cur_node = cur_node.next
        return counter

    def __getitem__(self, index):
        """
        Returns the item at <index>. Raised index error if index is out out of bound

        >>> items = [2, "google", 3, "apple", 4, "Amazon", 5, "Facebook"]
        >>> link = LinkedList(items)
        >>> link[5]
        'Amazon'
        >>> link[-3]
        'Amazon'
        >>> link[0]
        2
        >>> link[-1]
        'Facebook'
        >>> link[10]
        Traceback (most recent call last):
        IndexError
        """
        if (index < 0 and abs(index) > len(self)) or (index >= len(self)):
            raise IndexError
        else:
            if index < 0:
                index = len(self) + index
            counter, cur_node = 0, self._first
            while counter < index:
                cur_node = cur_node.next
                counter += 1
            return cur_node.item

    def reverse(self) -> None:
        """
        reverse linked linked list

        >>> items = [2, "google", 3, "apple", 4, "Amazon", 5, "Facebook"]
        >>> link = LinkedList(items)
        >>> link.reverse()
        >>> str(link)
        'Facebook -> 5 -> Amazon -> 4 -> apple -> 3 -> google -> 2'
        """
        cur_node, prev_node = self._first,None
        while cur_node:
            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node
        self._first = prev_node

    def __setitem__(self, key, value):
        """
        set item <value> at the index <key>. Raise index error if the index is out of bound.

        >>> items = [2, "google", 3, "apple", 4, "Amazon", 5, "Facebook"]
        >>> link = LinkedList(items)
        >>> str(link)
        '2 -> google -> 3 -> apple -> 4 -> Amazon -> 5 -> Facebook'
        >>> link[2] = "changed"
        >>> str(link)
        '2 -> google -> changed -> apple -> 4 -> Amazon -> 5 -> Facebook'
        """
        if ( key < 0 and abs(key) > len(self)) or (key >= len(self)):
            raise IndexError
        else:
            if key < 0:
                key = len(self) + key
            counter, cur_node = 0, self._first
            while counter < key:
                cur_node = cur_node.next
                counter += 1
            cur_node.item = value

    def __contains__(self, item) -> bool:
        """
        Returns True if this linked list contains <item>. Return False otherwise.

        >>> items = [2, "google", 3, "apple", 4, "Amazon", 5, "Facebook"]
        >>> link = LinkedList(items)
        >>> "Amazon" in link
        True
        >>> "bool" in link
        False
        """
        cur_node = self._first
        while cur_node:
            if cur_node.item == item:
                return True
            cur_node = cur_node.next
        return False

    def append(self, item) -> None:
        """
        Append a node with value as item to the end of this linked list

        >>> items = [2, "google", "changed", "apple", 4, "Amazon", 5, "Facebook"]
        >>> link = LinkedList(items)
        >>> str(link)
        '2 -> google -> changed -> apple -> 4 -> Amazon -> 5 -> Facebook'
        >>> link.append("Blue Chip")
        >>> str(link)
        '2 -> google -> changed -> apple -> 4 -> Amazon -> 5 -> Facebook -> Blue Chip'
        """
        new_node = _Node(item)
        prev, current = self._first, self._first
        while current:
            prev = current
            current = current.next
        prev.next = new_node


    def count(self, item) -> int:
        """
        Return the number of times <item> occurs.

        >>> link = LinkedList([2, 3, 2, 4, 2, 3, 5, 10, 4, "stock", "crypto", "stock"])
        >>> link.count(2)
        3
        >>> link.count(3)
        2
        >>> link.count("stock")
        2
        >>> link.count("black sheep")
        0
        """
        count, cur_node = 0, self._first
        while cur_node:
            if cur_node.item == item:
                count += 1
            cur_node = cur_node.next
        return count

    def pop(self) -> 'object':
        """
        Removes and returns the the last item of this linked list.
        >>> items = [2, 3, 4, 10, 20, 15, 9]
        >>> link = LinkedList(items)
        >>> link.pop()
        9
        >>> str(link)
        '2 -> 3 -> 4 -> 10 -> 20 -> 15'
        >>> linky = LinkedList([23])
        >>> linky.pop()
        23
        >>> str(linky)
        ''
        """
        if not self._first:
            raise IndexError
        else:
            hold = self._first.item
            if len(self) == 1:
                self._first = None
            else:
                prev_node, current_node, next_node = self._first, self._first, self._first.next
                while next_node:
                    prev_node = current_node
                    current_node, next_node = next_node, next_node.next
                hold = current_node.item
                prev_node.next = None
            return hold

    def extend(self, link: 'LinkedList') -> None:
        """
        >>> link1 = LinkedList([1, 2, 3, 5, 5, 6, 334, 234])
        >>> link2 = LinkedList(["hello", "New Line", "old line"])
        >>> link1.extend(link2)
        >>> str(link1)
        '1 -> 2 -> 3 -> 5 -> 5 -> 6 -> 334 -> 234 -> hello -> New Line -> old line'
        """
        if not self._first:
            self._first = link._first
        else:
            prev, current = self._first, self._first
            while current:
                prev, current = current, current.next
            prev.next = link._first

    def remove(self, item: 'objec') -> None:
        """
        Remove the first occurance of <item> from this linked list.
        If <item> not in the list, raise ValueError
        >>> link = LinkedList([3, 10, 39, 2, 50])
        >>> str(link)
        '3 -> 10 -> 39 -> 2 -> 50'
        >>> link.remove(2)
        >>> str(link)
        '3 -> 10 -> 39 -> 50'
        >>> link.remove(3)
        >>> str(link)
        '10 -> 39 -> 50'
        >>> link.remove(50)
        >>> str(link)
        '10 -> 39'
        """
        # when item is not in this linkedlist
        if not (item in self):
            raise ValueError
        # When item is the first element of this linked list
        elif self._first.item == item:
            self._first = self._first.next
        # When item is not the first item of this list but item is in the list
        else:
            prev, current = None, self._first
            while current.item != item:
                prev, current = current, current.next
            prev.next = current.next


    def insert(self, index: int, value: 'object') -> None:
        """
        insert the  given item at the given index in this linked list

        >>> link = LinkedList([3, 10, 39, 2, 50])
        >>> str(link)
        '3 -> 10 -> 39 -> 2 -> 50'
        >>> link.insert(1, 100)
        >>> str(link)
        '3 -> 100 -> 10 -> 39 -> 2 -> 50'
        """
        if not self._first:
            self._first = _Node(value)
        else:
            new_node = _Node(value)
            curr_node = self._first
            if index == 0:
                new_node.next = curr_node
                self._first = new_node
            elif len(self) <= index:
                while curr_node.next:
                    curr_node = curr_node.next
                curr_node.next = new_node
            else:
                count, prev = 0, None
                while count < index:
                    prev, curr_node = curr_node, curr_node.next
                    count += 1
                prev.next,new_node.next = new_node, curr_node


if __name__ == "__main__":
    import doctest
    doctest.testmod()
