# Hash Sort

## Hypothesis

The hypothesis for this project is whether or not hashing could be a valid strategy in achieving a linear time sorting algorithm. Since adding to a hash table is an `O(1)` operation then adding n items to a hash table would be a linear operation or `O(n)`. The limiting step here then becomes generating a hash that enables the sorting behavior. For example, if the table were to be given values of `z` and `a` in that order, the expected outcome would be that the hash function would provide a value in which `a` came before `z`. As examples become more complex, the hash function becomes a bit more difficult than just mapping characters to a value. That said, I believe that there likely are functions out there that would better handle these cases than ones that I had considered. Since the hash table, in this scenario, would always be in a sorted state, collecting the values from the hash table would also be an `O(n)` operation. Or more accurately would likely be in the order of the size of the hash table. This would of course be linear and thus still of a linear time complexity. In order for this hypothesis to succeed, the two major factors are the space-time trade off and an effective/efficient hash function.

## Implementation

As mentioned, the first of the two factors for this hypothesis is that there is a space-time trade off. To create a general purpose implementation of this idea, I would either have to limit the size of the strings or assume that strings could be in a sorted state past `k` characters. Under both assumptions, this algorithm would be incredibly limited and thus not very useful. In this implementation, I decided that I would create more of a tree-like structure in which strings are sorted to a specific accuracy. Past this accuracy, strings are considerd as collisions which are then added to a linked list. This also accounts somewhat for the issue of having an effective/efficient hash function as well as there is less of a necessity for the hash function to sort without collisions.

Due to this concession, this causes the time complexity to increase to `O(nlog(n))` because of the tree-like structure as well as the sorting algorithm that must be employed to sort the leaf node, linked lists. This is currently being done using a merge sort which has a time complexity of `O(nlog(n))` making the entire hash sort algorithm the same. This makes it much more generalizable and there is likely plenty of area for optimization; notably, the hash function could be improved to decrease the number of layers in the hash table tree.

## Sort timings

10,000 strings
Insertion sort -- 5.72 seconds
Quick sort -- 0.02 seconds
Merge sort -- 0.04 seconds
Hash sort -- 0.11 seconds
