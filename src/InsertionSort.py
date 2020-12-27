import time
from List import List


def insertion_sort(a):
    """
    This is a simple implementation of insertion sort.

    `Complexity`: O(n^2)\n
    `Memory`: In place\n
    `Stability`: Stable\n

    Args:
        a (string[]|integer[]): an unsorted array or list of strings or integers

    Returns:
        string[]|integer[]: a sorted array or list of strings or integers
    """

    if type(a) == List:
        node = a.get_head().get_next()
        while node != None:
            z = node
            while z.has_previous():
                # Get nodes
                nxtlst = z.get_previous().get_previous()
                lst = z.get_previous()
                cur = z
                nxt = z.get_next()

                # If the current value needs to be moved
                if lst.get_value() > cur.get_value():
                    if nxt != None:
                        nxt.set_previous(lst)
                    else:
                        a.set_tail(cur)
                    lst.set_next(nxt)
                    lst.set_previous(cur)
                    if nxtlst != None:
                        nxtlst.set_next(cur)
                    else:
                        a.set_head(cur)
                    cur.set_previous(nxtlst)
                    cur.set_next(lst)
                else:
                    break
                z = cur
            node = node.get_next()
        return a
    else:
        for i, f in enumerate(a):
            if i == 0:
                continue
            # Iterate from the current node back towards the first node swapping values when necessary
            n = i
            while n >= 1:
                # if the previous value is greater than the current value
                # swap the two values. else no more swapping is required
                if a[n - 1] > a[n]:
                    tmp = a[n]
                    a[n] = a[n - 1]
                    a[n - 1] = tmp
                    n -= 1
                else:
                    break
    return a