import time
from List import List
from ListItem import ListItem

class HashSort:
    """
    A data structure that exists in a constantly sorted state. Sorting, therefore, is done
    whenever a value is added to the structure.

    Drawbacks:\n
    \tOnly handles alphanumerics -- bounded by memory availability
    \tMemory utilization is incredibly inefficient due to the potentially sparse nature of the structure

    `Complexity`:\n
    \tAdd item (worst): O(n)\n
    \tAdd item (average): O(1)\n
    \tBuilding table: O(n)\n
    \tSorting: structure is always sorted\n
    `Memory`: Not in place\n
    `Stability`: Stable\n
    `Space`: O(36^accuracy)
    """
    def __init__(self, values=[], accuracy=5):
        # first 36 spaces are unused
        self._factor = 37
        self._table = [None] * ((self._factor ** accuracy))
        self._accuracy = min(accuracy, 5)  # DO NOT GO OVER 5, TRUST ME
        self.length = 0
        if len(values) > 0:
            for v in values:
                self.add(v)

    def _hash(self, value):
        # Reverse weight string hashes such that later characters apply less value
        h = i = 0
        while i < self._accuracy and i < len(value):
            c = value.strip().replace(" ", "").lower()[i]  # character
            cv = ord(c)
            if cv >= 97 and cv <= 122:
                cv -= 87
            elif cv >= 48 and cv <= 57:
                cv -= 48
            else:
                raise Exception("Invalid character (`%c`)" % c)
            h += (self._factor ** (self._accuracy - i - 1)) * (cv + 1)
            i += 1
        return h

    def add(self, value):
        h = self._hash(value)
        if self._table[h] == None:
            self._table[h] = List()
        self._table[h].insert_sorted(ListItem(value))
        self.length += 1
        return True

    def get_values(self):
        v = []
        for r in self._table:
            if r != None:
                v += r.get_items()
        return v

    def __len__(self):
        return self.length