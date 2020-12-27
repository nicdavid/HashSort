from List import List
from ListItem import ListItem
from MergeSort import merge_sort

"""
Hash Table

Sorting strings is O(n) time.
It ends up actually being nlogk(max length of string). But since the 
length of the string is going to be a relatively low number, the length
of the string will not cause the asymtotic behavior to change.


Overview:
This implementation of the hash table is what allows for the
sorting to occur. I have created my own version of a hash table
because hash tables are implemented as dictionaries in Python.
This does not allow for the sorting effect that I am able to
acheive using this implementation.

When created, the hash table creates a table (an array) of 
a specified size. This table is initialized with the value
None in all of the positions. I also initialize the length
of the table here.

The width refers to how many characters will be sorted through
when sorting string values. The larger this number becomes, the
more space that is required by the hash table. Smaller width's
will utilize less space, but will not gaurantee that the array 
will be sorted fully.

The getSize function computes the sum of values from 1 to k where
k is the number of characters to be sorted on. This is a sum because
we will need the space for any length of string from 1 to k. For
example, if k were 2, we would need 26^1 spaces to represent the 
26 one character strings as well as 26^2 to represent the 676
two character strings.

The hash function that is currently implemented is fairly rudimentary.
For integers, it will return the integer as the hashed value. For strings,
the hashed value returns the numerical value of each of the characters which
are weighted by the position that it exists in the string and by the iteration
count. This ensures that strings are sorted according to their alphabetical 
ordering. Any hash function can be used as long as it returns an integer value.

The append function will take in the value to be appended and will hash it.
Once hashed, the hashed value is checked in the hash table. If a list does not
yet exist in this location, one is created. Once created, the value is added 
to the list. If a hashed value falls outside of the bounds of the array, it
will place it in the list on the end of the hash table. For example, if the 
largest value in the hash table is n and a hashed value turns out to be n+2,
that value will be placed in the list for n. This means that ends of the list
will not be sorted, but the algorithm may be rerun on the beginning and ends
of the hash table to ensure total sorting.

The getValues function allows the program to pull the sorted values from the
hash table as an array. Since the hash table will likely be very sparse for
a small or an undiverse input, there will be many 'None' values in the table.
This will remove the 'None' values, ensure that all values are out of the 
collision lists, and relinquishes the need to hold the large amount of space
that the hash table takes up. In this scenario, the space the hash table uses
is not freed, but I can envision that it may be in the future.

The len and str functions provide methods for determining length and converting
the structure into string form respectively. These methods are used when the
built in len() and print() functions are called respectively.


Integer Drawbacks:
There are a couple fallbacks here. The first being that the
integer values that are being sorted may not have a range from 
0 to n where n is the max number of array slots. This is an issue 
that can be addressed in a couple different ways. The first being
that a larger array may be used. This seems like a waste of memory,
but is one possibility.

The next solution that will mitigate space waste is to run through 
the list and find bounds. If for instance, the lowest value that 
needs to be sorted is 1000, we can pretend that the 0 value of the 
table is where 1000 should be placed. This allows for an extra 1000
values (n+1000 values) to be represented in the table.

The next issue that I face with this implementation when sorting 
integers is the range of values that can be sorted. For example, 
if the values to be sorted range from 0-n, but there are only n/2
spots in the array (representing values 0-n/2), values in the upper
n/2 range will not be placed in the table. This will result in a 
null pointer exception because the array slot does not exist. I am
currently addressing this issue by simply appending values that appear 
outside of the range (0-n/2) to the end of the list contained in the 
n/2th table slot. This leads to a lack of sorting for the entirety of
the unsorted items. This can then be addressed using the strategy in 
the previous paragraph. You are able to take the values in table slot
n/2 and run the hash sort algorithm on that individual slot. The lower 
bound of the array can be set to n/2 and now the second iteration of the
hash sort will run on the values that were not sorted in the first run.


String Drawbacks:
Strings are sortable in O(n) using this implementation. The drawbacks
are that for large enough unsorted data samples, there is a low granularity
for the sorted values. By this, I mean that there is a tradeoff between
table size and how many characters can be sorted. For example, to sort strings
based on the first four characters, you must have an array of 26^4 size.

To address this issue, a similar strategy can be applied as in the integer
cases. After the first run through, strings should be sorted roughly based 
on the  first k characters. Once the strings are sorted in this degree, you 
may then run the hash sort algorithm on buckets of n/2 size. This will allow
you to increase the number of characters (the width) that are being used 
when sorting.

Another performance increase to this process is by setting the bounds of the
hash table. After the first iteration has run, we know that the first k characters
of every word have been sorted. This means that we can set the 0th position in
the table to account for the fact that we don't need to sort by those characters.

Although this approach to sorting does not sort every word properly in the first
run, it should still take O(n) time. The buckets that are used when fully sorting
are dependent on how much memory one is willing to utilize as well as the length
of the words. I have not worked out the exact math here, but I do not believe 
this will cause it to approach O(nlgn) time.


Other Drawbacks:
I have not tested this method with anything other than positive integers. I 
believe that with this strategy, it is possible to develop a hash function
for any other scenario to make this sorting method work.

Large files that cannot be read into memory may also prove to have issues.
I anticipate that for a large enough data source, the strategies provided
above will not work. I am certain that there is possibility for a workaround
using physical storage. By this I mean one can treat a portion of physical 
memory as the hash table. You are able to read a portion of the large file
into memory and then sort it and then read the whole bucket back into physical
memory. This strategy could allow for a much larger hash table as physical 
memory is much larger and removes space constraints. This will allow for 
the large file to be sorted.


Updates:
Hash sort sorts values once into a hash table and then when the user
calls getValues() the lists will be sorted using insertion sort. According
to bucket sort, this should maintain O(n) for the average time complexity.
For integers, values will potentially overwhelmingly fall outside of the 
hash table range (0 - 26^6), so there may be many values in the 26^6-1 table
slot. This may be addressed by running through the values and computing
a range and then using a range to find bounds for the hash table. By this,
I mean that you can offset the array to be able to encompass more values in
the table, so the table isn't overwhelmingly skewed to one side.

"""


class HashTable:
    """
    Hash sort implementation that implements hash tables in a tree form. Nodes are linked lists of values that collide.

    `Complexity`:\n
    \tAdd item: O(1)\n
    \tBuilding table: O(n)\n
    \tSorting: O(nlog(n))\n
    `Memory`: Not in place\n
    `Stability`: Stable\n
    """

    def __init__(self, values=[], accuracy=6, offset=0):
        self._table = [None] * 128
        self.length = 0
        self._accuracy = accuracy - 1
        self._offset = offset
        if len(values) > 0:
            for v in values:
                self.add(v)

    def get_accuracy(self):
        """
        Return the defined accuracy.

        Returns:
            integer: Integer value of the accuracy.
        """
        return self._accuracy + 1

    def _hash(self, value):
        """
        Simple hash function.

        Args:
            value (string|integer): value to be hashed

        Returns:
            integer: integer hash of the value
        """
        if type(value) == str:
            if len(value) <= self._offset:
                return 0
            val = value.strip().replace(" ", "").lower()[self._offset]
            return ord(val)
        else:
            return value // 128

    def add(self, value):
        """
        Adds a value to the hash table.

        Args:
            value (string|integer): value to add to the hash table

        Returns:
            boolean: whether or not the addition succeeds
        """
        if type(value) != str and type(value) != int:
            return False
        v = self._hash(value)
        # Add value to sub-table else add to the current table as a list item
        if self._offset < self._accuracy:
            if self._table[v] == None:
                self._table[v] = HashTable(
                    accuracy=self._accuracy, offset=self._offset + 1
                )
            self._table[v].add(value)
        else:
            if self._table[v] == None:
                self._table[v] = List()
            self._table[v].append(ListItem(value))
        self.length += 1
        return True

    def get_values(self):
        """
        returns a list of the values in the hash table.

        Returns:
            array: array of values
        """
        values = []
        for i, r in enumerate(self._table):
            if r != None:
                if type(r) == HashTable:
                    values += r.get_values()
                elif type(r) == List:
                    values.append(r.get_items())
        return values

    def _sort_list(self, l):
        """
        Sorts a leaf node (list).

        Args:
            l (List): list of items

        Returns:
            list: sorted list of items
        """
        return merge_sort(l)

    def sort(self):
        """
        Recursively sorts the hash table

        Returns:
            boolean: whether the sorting succeeds or not
        """
        # If the hash map tree contains no values don't try to sort it
        if self.length == 0:
            return True

        # Iterate through all of the elements of the table list
        for i, r in enumerate(self._table):
            if r != None:
                if type(r) == HashTable:
                    r.sort()
                elif type(r) == List:
                    self._table[i] = self._sort_list(r)
        return True

    def __len__(self):
        return self.length

    def __str__(self):
        return str(self.get_values())