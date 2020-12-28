# Hash Sort

## Hypothesis

The hypothesis for this project is whether or not hashing could be a valid strategy in achieving a linear time sorting algorithm. Since adding to a hash table is an `O(1)` operation then adding `n` items to a hash table would be a linear operation or `O(n)`. Since the sorting functionality is provided at the time of adding an item, then technically, the sorting can be extrapolated to be `O(n)` as well. The major drawback of this approach is that it requires a large amount of memory to be utilized to its fullest potential. This memory usage can be calculated as `# supported characters ^ accuracy` where the number of supported characters is the number of characters that could be sorted upon (ie. 36 for alphanumerics) and the accuracy is the number of characters in each string to generate a hash for. For example, to sort a list of alphanumerics with a maximum length of 4, the total space utilization will be `36^4=1,679,616`.

### Use Cases

1. Constant data stream -- This data structure could be used is in situations with data streaming from many sources. Instead of applying a sort function on a data structure in a routine manner, this will provide a constantly sorted data format. Ideally, the data would be streamed from an external source and thus there wouldn't necessarily be any real data redundancy required when adding to the table.

2. Repetitive Sorting -- In situations in which a data set must be repetitively sorted to maintain a sorted integrity, this could be a good work around. For larger data sets, it becomes much more time consuming to sort. Since this structure is constantly sorted, there is never a need to run a sort as it will retain sorted format upon every entry into the structure.

### Drawbacks

1. Memory utilization -- for smaller or more predictable data sets, this structure will be incredibly sparse and thus the memory required will not be used optimally.

2. Memory bounding -- the theoretical data structure would require an infinite amount of memory to sort infinitely long strings, thus, the "sorting accuracy" is bounded by memory. This can be worked around by providing a constantly sorted list to handle possible collisions.

## Sort timings (10 run average)

Parameters:
`STRING_LENGTH=12`
`ACCURACY=6`

NOTE: For consistency, the times below are collected using alphanumeric values `[0-9a-z]` as the current implementation of the hash sort only handles alphanumerics.

1,000 strings
Insertion sort -- 0.32 seconds
Quick sort -- 0.003 seconds
Merge sort -- 0.011 seconds
Hash sort -- 0.580 seconds

10,000 strings
Insertion sort -- 58.096 seconds
Quick sort -- 0.077 seconds
Merge sort -- 0.285 seconds
Hash sort -- 0.747 seconds

100,000 strings
Insertion sort -- ...
Quick sort -- 2.675 seconds
Merge sort -- 5.497 seconds
Hash sort -- 2.027 seconds

1,000,000 strings
Insertion sort -- ...
Quick sort -- 36.726 seconds
Merge sort -- 10.961 seconds
Hash sort -- 8.791 seconds

10,000,000 strings
Insertion sort -- ...
Quick sort -- 509.120 seconds
Merge sort -- ...
Hash sort -- 82.122 seconds
