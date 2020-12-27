class ListItem:
    """
    A list item contains a previous and next node reference. This will
    allow for two-way traversal through the list. The value of the list
    item is also stored.
    """

    def __init__(self, v):
        self._prev = None
        self._next = None
        self._value = v

    def get_value(self):
        return self._value

    def set_next(self, i):
        self._next = i
        return True

    def get_next(self):
        return self._next

    def has_next(self):
        return self._next != None

    def has_previous(self):
        return self._previous != None

    def set_previous(self, i):
        self._prev = i
        return True

    def get_previous(self):
        return self._prev

    def has_previous(self):
        return self._prev != None

    def __str__(self):
        return self._value