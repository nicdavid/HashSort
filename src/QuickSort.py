from List import List


def _partition(a, l, h):
    i = l - 1
    pivot = a[h]
    for j in range(l, h):
        if a[j] <= pivot:
            i = i + 1
            tmp = a[i]
            a[i] = a[j]
            a[j] = tmp
    tmp = a[i + 1]
    a[i + 1] = a[h]
    a[h] = tmp
    return i + 1


def quick_sort(a, l, h):
    """
    This is a simple implementation of insertion sort.

    `Complexity (avg)`: O(nlog(n))\n
    `Memory`: In place\n
    `Stability`: Unstable\n

    Args:
        a (string[]|integer[]): array of strings or integers
        l (integer): lower bound of the partition
        h (integer): upper bound of the partition

    Raises:
        Exception: throws an exception if a linked list is supplied as a parameter

    Returns:
        string[]|integer[]: string or integer array of sorted values
    """

    if type(a) == List:
        raise Exception("Cannot run quick sort on a linked list.")

    if l < h:
        pivot = _partition(a, l, h)
        quick_sort(a, l, pivot - 1)
        quick_sort(a, pivot + 1, h)
    return a