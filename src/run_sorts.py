import random
import string
import time
import sys
import queue
from threading import Thread
from HashTable import HashTable
from List import List
from ListItem import ListItem
from QuickSort import quick_sort
from InsertionSort import insertion_sort
from MergeSort import merge_sort
from VerifySort import verify_sort

# Total values to sort
TOTAL = 10000

# How many values to account for while sorting with a hash table
ACCURACY = 6

# Width of the sortable strings
STRING_WIDTH = 12


def run_sort(n):
    output = [0, 0, 0, 0]

    # Creates two arrays -- one with strings and the other integers.
    a = []
    b = []
    print("Generating " + str(n) + " items...")
    for i in range(0, n):
        s = ""
        for j in range(0, STRING_WIDTH):
            s += random.choice(string.ascii_letters)
        a.append(s.lower())
        num = random.randint(0, n - 1)
        b.append(num)
    print("Finished generating items.\n\n")

    # Insertion sort
    if n <= 10000:
        print("Running insertion sort...")
        insertion_a = a.copy()
        st = time.time()
        insertion_sorted = insertion_sort(insertion_a)
        output[0] = time.time() - st
        print("Sort took a total of %s seconds" % str(time.time() - st))
        verify_sort(insertion_sorted)
        print("\n")
    else:
        print(
            "Insertion sort only runs up to a value of 100000 otherwise it takes too long."
        )
        print("\n")

    # Quick sort
    print("Running quick sort...")
    quick_a = a.copy()
    st = time.time()
    quick_sorted = quick_sort(quick_a, 0, len(quick_a) - 1)
    output[1] = time.time() - st
    print("Sort took a total of %s seconds" % str(time.time() - st))
    verify_sort(quick_sorted)
    print("\n")

    # Merge sort
    print("Running merge sort...")
    merge_a = a.copy()
    st = time.time()
    merge_sorted = merge_sort(merge_a)
    output[2] = time.time() - st
    print("Sort took a total of %s seconds" % str(time.time() - st))
    verify_sort(merge_sorted)
    print("\n")

    # Hash sort
    print("Running hash sort...")
    hash_a = a.copy()
    st = time.time()
    t = HashTable(values=hash_a, accuracy=ACCURACY)
    t.sort()
    output[3] = time.time() - st
    print("Sort took a total of %s seconds" % str(time.time() - st))
    hash_sorted = t.get_values()
    verify_sort(hash_sorted)
    print("\n")

    return output


RUN_TOTALS = [1000, 10000, 100000, 1000000]
sort_data = {
    "insertion": {"1000": [], "10000": [], "100000": [], "1000000": []},
    "quick": {"1000": [], "10000": [], "100000": [], "1000000": []},
    "merge": {"1000": [], "10000": [], "100000": [], "1000000": []},
    "hash": {"1000": [], "10000": [], "100000": [], "1000000": []},
}


RUNS = 10
print("Running tests. Please wait...\n")

# Save stdout
stdout_saved = sys.stdout

# Start Runs
for n in RUN_TOTALS:
    # Restore stdout
    sys.stdout = stdout_saved

    print("Running sorts with %d items" % n)

    que = queue.Queue()
    threads = list()

    # Silence stdout
    sys.stdout = open("sort-run.log", "a")
    for r in range(0, RUNS):
        t = Thread(target=lambda q, arg1: q.put(run_sort(arg1)), args=(que, n))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    while not que.empty():
        run = que.get()
        sort_data["insertion"][str(n)].append(run[0])
        sort_data["quick"][str(n)].append(run[1])
        sort_data["merge"][str(n)].append(run[2])
        sort_data["hash"][str(n)].append(run[3])

# Restore stdout
sys.stdout = stdout_saved

print("\n\nSORT RUN RECEIPT (%d RUNS)" % RUNS)
print(
    "------------------------------------------------------------------------------------------"
)
for v in sort_data.keys():
    for n in sort_data[v].keys():
        if len(sort_data[v][n]) != 0:
            print(
                "Sort: %s\t\t|\tValues: %s\t\t|\tAverage: %f"
                % (v, n, sum(sort_data[v][n]) / len(sort_data[v][n]))
            )
    print(
        "------------------------------------------------------------------------------------------"
    )
