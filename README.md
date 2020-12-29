# Hash Sort

The hypothesis for this project is whether or not hashing could be a valid strategy in achieving a linear time sorting algorithm. Since adding to a hash table is an `O(1)` operation then adding `n` items to a hash table would be a linear operation or `O(n)`. Since the sorting functionality is provided at the time of adding an item, then technically, the sorting can be extrapolated to be `O(n)` as well. The major drawback of this approach is that it requires a large amount of memory to be utilized to its fullest potential. This memory usage can be calculated as `# supported characters ^ accuracy` where the number of supported characters is the number of characters that could be sorted upon (ie. 36 for alphanumerics) and the accuracy is the number of characters in each string to generate a hash for. For example, to sort a list of alphanumerics with a maximum length of 4, the total space utilization will be `36^4=1,679,616`.

### Use Cases

1. Constant data stream -- This data structure could be used is in situations with data streaming from many sources. Instead of applying a sort function on a data structure in a routine manner, this will provide a constantly sorted data format. Ideally, the data would be streamed from an external source and thus there wouldn't necessarily be any real data redundancy required when adding to the table.

2. Repetitive Sorting -- In situations in which a data set must be repetitively sorted to maintain a sorted integrity, this could be a good work around. For larger data sets, it becomes much more time consuming to sort. Since this structure is constantly sorted, there is never a need to run a sort as it will retain sorted format upon every entry into the structure.

### Drawbacks

1. Memory utilization -- for smaller or more predictable data sets, this structure will be incredibly sparse and thus the memory required will not be used optimally.

2. Memory bounding -- the theoretical data structure would require an infinite amount of memory to sort infinitely long strings, thus, the "sorting accuracy" is bounded by memory. This can be worked around by providing a constantly sorted list to handle possible collisions.

## Sort timings (10 run average)

Parameters: `STRING_LENGTH=12` `ACCURACY=6`

NOTE: For consistency, the times below are collected using alphanumeric values `[0-9a-z]` as the current implementation of the hash sort only handles alphanumerics.

<br>

| Sort      | Values (n) | Average (s) |
| --------- | ---------: | ----------: |
| Insertion |      1,000 |    0.330017 |
| Insertion |     10,000 |    58.09600 |
| Insertion |    100,000 |         --- |
| Insertion |  1,000,000 |         --- |
| Insertion | 10,000,000 |         --- |

<br>

| Sort  | Values (n) | Average (s) |
| ----- | ---------: | ----------: |
| Quick |      1,000 |    0.006882 |
| Quick |     10,000 |    0.219812 |
| Quick |    100,000 |    2.591667 |
| Quick |  1,000,000 |   37.517032 |
| Quick | 10,000,000 |  510.159192 |

<br>

| Sort  | Values (n) | Average (s) |
| ----- | ---------: | ----------: |
| Merge |      1,000 |    0.010272 |
| Merge |     10,000 |    0.474531 |
| Merge |    100,000 |    5.238785 |
| Merge |  1,000,000 |   60.483092 |
| Merge | 10,000,000 |         --- |

<br>

| Sort | Values (n) | Average (s) |
| ---- | ---------: | ----------: |
| Hash |      1,000 |    0.571172 |
| Hash |     10,000 |    0.720872 |
| Hash |    100,000 |    2.074849 |
| Hash |  1,000,000 |    9.441541 |
| Hash | 10,000,000 |   83.536418 |
