from ListItem import ListItem


class List:
    """
    A simple linked list implementation. The list object contains the head, tail, and
    the length of the list. I keep track of the tail of the list
    so that I can append items to the list in O(1) time.
    """

    def __init__(self):
        self._head = None
        self._tail = None
        self.length = 0

    def get_head(self):
        return self._head

    def get_tail(self):
        return self._tail

    def set_head(self, n):
        self._head = n

    def set_tail(self, n):
        self._tail = n

    def append(self, li):
        """
        Add an item to the linked list.

        Args:
            li (string|integer): a list item to add to the list

        Returns:
            boolean: whether or not the value is sucessfully appended to the list
        """
        if self._head == None:
            self._head = li
        elif self._tail == None:
            self._tail = li
            self._head.set_next(li)
            self._tail.set_previous(self._head)
        else:
            li.set_previous(self._tail)
            self._tail.set_next(li)
            self._tail = li
        self.length += 1
        return True

    def insert_sorted(self, li):
        node = self._head
        if self._head == None:
            self._head = li
        elif self._tail == None:
            if li.get_value() < self._head.get_value():
                self._head.set_previous(li)
                li.set_next(self._head)
                self._tail = self._head
                self._head = li
            else:
                self._tail = li
                self._head.set_next(li)
                self._tail.set_previous(self._head)
        elif li.get_value() < self._head.get_value():
            li.set_next(self._head)
            self._head.set_previous(li)
            self._head = li
        elif li.get_value() >= self._tail.get_value():
            li.set_previous(self._tail)
            self._tail.set_next(li)
            self._tail = li
        else:
            node = node.get_next()
            while node != None:
                if li.get_value() < node.get_value():
                    prev = node.get_previous()
                    newnxt = node
                    li.set_next(newnxt)
                    newnxt.set_previous(li)
                    li.set_previous(prev)
                    prev.set_next(li)
                    break
                node = node.get_next()
        self.length += 1
        return True

    def get_items(self):
        """
        Builds an array of the values in the list.

        Returns:
            array: array representation of the values in the linked list
        """
        if self.length == 0 or self._head == None:
            return []
        a = [self._head.get_value()]
        i = self._head
        while i.has_next():
            i = i.get_next()
            a.append(i.get_value())
        return a

    def get_string(self):
        if self.length == 0 or self._head == None:
            return ""
        s = self._head.get_value()
        i = self._head
        while i.has_next():
            i = i.get_next()
            s += ", %s" % i.get_value()
        return s

    def __len__(self):
        return self.length

    def __str__(self):
        return self.get_string()