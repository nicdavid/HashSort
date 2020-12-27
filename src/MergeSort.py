from List import List
from ListItem import ListItem


def merge_sort(a):
    """
    This is a simple implementation of insertion sort.

    `Complexity`: O(nlog(n))\n
    `Memory`: Not in place\n
    `Stability`: Stable\n

    Args:
        a (string[]|integer[]): an unsorted array or List of strings or integers

    Returns:
        string[]|integer[]: sorted array or list of string or integers
    """
    if len(a) <= 1:
        return a
    if type(a) == List:
        node = a.get_head()
        i = 0
        left = List()
        right = List()
        while i < len(a):
            if i < len(a) // 2:
                left.append(ListItem(node.get_value()))
            elif i >= len(a) // 2:
                right.append(ListItem(node.get_value()))
            node = node.get_next()
            i += 1

        # Sort the two halves of the array
        k = List()
        sorted_l = merge_sort(left)
        sorted_r = merge_sort(right)
        i = sorted_l.get_head()
        j = sorted_r.get_head()
        while i is not None and j is not None:
            if i.get_value() < j.get_value():
                k.append(ListItem(i.get_value()))
                i = i.get_next()
            else:
                k.append(ListItem(j.get_value()))
                j = j.get_next()

        # Checking if any element was left
        while i is not None:
            k.append(ListItem(i.get_value()))
            i = i.get_next()

        while j is not None:
            k.append(ListItem(j.get_value()))
            j = j.get_next()

        return k
    else:
        mid_idx = len(a) // 2
        left = a[:mid_idx]
        right = a[mid_idx:]

        sorted_l = merge_sort(left)
        sorted_r = merge_sort(right)
        # Sort the two halves of the arrays
        i = j = 0
        k = []
        while i < len(sorted_l) and j < len(sorted_r):
            if sorted_l[i] < sorted_r[j]:
                k.append(sorted_l[i])
                i += 1
            else:
                k.append(sorted_r[j])
                j += 1

        # Checking if any element was left
        while i < len(sorted_l):
            k.append(sorted_l[i])
            i += 1

        while j < len(sorted_r):
            k.append(sorted_r[j])
            j += 1

        return k
